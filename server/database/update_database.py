import yfinance as yf

from logger import status_message
from repository import db_op
from utilities import DBOperationError, StockDataFetchError


def update_stock_datas():

    db_op.open_connection_db()
    status_message("Mit Datenbank verbunden.")
    result = db_op.execute("SELECT * FROM stocks").fetchall()

    status_message("Börsendaten werden abgerufen - update_stock_datas()")
    for dsatz in result:
        isin = dsatz[0]
        ticker_symbol = f"{dsatz[1]}.DE"
        name = dsatz[2]

        try:
            ticker_data = yf.Ticker(ticker_symbol)
            historical_data = ticker_data.history(period='2y')
            status_message(f"Aktuell für {name} Symbol:{ticker_symbol}", False)

        except Exception as e:
            error_msg = ("Keine Börsendaten von 'yfinance'.\n"
                         "Ort: update_stock_datas (update_database.py)\n"
                         f"Error: {str(e)}\n")
            raise StockDataFetchError(error_msg) from e
        success = True
        # print(historical_data)
        for i, row in historical_data.iterrows():

            values = {"isin": isin,
                      "date": i.strftime('%Y-%m-%d'),
                      "open": row['Open'],
                      "high": row['High'],
                      "low": row['Low'],
                      "close": row['Close'],
                      "volume": row['Volume'],
                      "dividends": row['Dividends'],
                      "stock_splits": row['Stock Splits']}

            if success:
                sql = """INSERT INTO stock_data(
                                    isin,
                                    date,
                                    open,
                                    high,
                                    low,
                                    close,
                                    volume,
                                    dividends,
                                    stock_splits)
                                VALUES (:isin,
                                        :date,
                                        :open,
                                        :high,
                                        :low,
                                        :close,
                                        :volume,
                                        :dividends,
                                        :stock_splits)"""

                success = db_op.execute_return_bool(sql, values)
                status_message(f"Füge Daten ein - ISIN: {isin}", False)

            if success is False:

                try:
                    sql = """UPDATE stock_data
                                SET isin = :isin,
                                    open = :open,
                                    high = :high,
                                    low = :low,
                                    close = :close,
                                    volume = :volume,
                                    dividends = :dividends,
                                    stock_splits = :stock_splits
                                WHERE isin = :isin and date = :date"""

                    db_op.execute_and_commit(sql, values)
                    status_message(f"Aktualisiere Daten - ISIN: {isin}", False)
                    success = True
                    break

                except DBOperationError as e:
                    print(f"Fehler Daten von {name} isin: {isin} konnte nicht eingetragen werden")
                    raise DBOperationError("feheler") from e
                except Exception as e:
                    raise Exception from e

    db_op.close()
    status_message("Daten erfolgreich eingefügt.")
