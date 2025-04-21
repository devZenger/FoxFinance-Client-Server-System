import os
import sqlite3
import yfinance as yf

from repository import DBExecutor, simple_search


def update_stock_datas():

    path = os.path.join("..", "server", "database", "FoxFinanceData.db")

    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        print("verbunden")
    except:
        print("Konnte keine Verbindung herstellen")

    cursor.execute("SELECT * FROM stocks")

    result = cursor.fetchall()

    for dsatz in result:
        isin = dsatz[0]
        ticker_symbol = f"{dsatz[1]}.DE"
        name = dsatz[2]

        try:
            ticker_data = yf.Ticker(ticker_symbol)
            historical_data = ticker_data.history(period='2y')
        except:
            print("Fehler konnte keine Daten zum Ticker Symbol finden")

        for i, row in historical_data.iterrows():

                values = (isin, i.strftime('%Y-%m-%d'),
                        row['Open'],
                        row['High'],
                        row['Low'],
                        row['Close'],
                        row['Volume'],
                        row['Dividends'],
                        row['Stock Splits'])

                try:
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
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

                    cursor.execute(sql, values)
                    connection.commit()
                    print(f"Insert isin: {isin}")

                except:
                    last_row_id = cursor.lastrowid

                    try:
                        sql= f"""UPDATE stock_data 
                                    SET isin = ?,
                                        date = ?,
                                        open = ?,
                                        high = ?,
                                        low = ?,
                                        close = ?,
                                        volume = ?,
                                        dividends = ?,
                                        stock_splits = ?
                                    WHERE  dataID = {last_row_id}"""

                        cursor.execute(sql, values)
                        connection.commit()
                        print(f"Updated isin: {isin}")

                        break

                    except:
                        print(f"Fehler Daten von {name} isin: {isin} konnte nicht eingetragen werden")

    connection.close()


def update_single_stock_datas(isin):

    stock_info = simple_search("stocks", "isin", isin)

    print(stock_info)

    ticker_symbol = f"{stock_info["row_result0"]["ticker_symbol"]}.DE"
    ticker_data = yf.Ticker(ticker_symbol)
    historical_data = ticker_data.history(period='1d')

    row = historical_data.iloc[0]

    date = str(row.name.strftime('%Y-%m-%d'))
    print(date)

    values = (row['Open'],
              row['High'],
              row['Low'],
              row['Close'],
              row['Volume'],
              row['Dividends'],
              row['Stock Splits'],
              isin,
              row.name.strftime('%Y-%m-%d')
             )

    sql = """UPDATE stock_data 
                SET open = ?,
                    high = ?,
                    low = ?,
                    close = ?,
                    volume = ?,
                    dividends = ?,
                    stock_splits = ?
                WHERE isin = ? and date = ?"""

    db_ex = DBExecutor()
    db_ex.open_connection_db()
    db_ex.execute_and_commit(sql, values)
    db_ex.close()


if __name__ == "__main__":

    isin = "DE000ENAG999"

    answer = update_single_stock_datas(isin)

    print(" ")
    print(answer)
