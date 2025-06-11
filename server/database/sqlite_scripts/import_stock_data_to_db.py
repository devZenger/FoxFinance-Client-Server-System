import os
import sys
import sqlite3
import yfinance as yf


def insert_stock_datas(path):

    try:
        connection = sqlite3.connect(path)

    except sqlite3.Error as e:
        error_msg = ("Verbindungsprobleme mit der Datenbank\n"
                     f"Pfad: {path}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stocks")

    result = cursor.fetchall()

    for dsatz in result:
        isin = dsatz[0]
        ticker_symbol = f"{dsatz[1]}.DE"
        name = dsatz[2]

        try:
            ticker_data = yf.Ticker(ticker_symbol)
            historical_data = ticker_data.history(period='6y')
        except Exception as e:
            error_msg = ("Börsendaten konnten nicht abgerufen werden.\n"
                         f"Ticker Symbol: {ticker_symbol}\n"
                         f"Error: {str(e)}\n")
            raise RuntimeError(error_msg) from e

        current_name = ""
        for i, row in historical_data.iterrows():
            try:
                if name != current_name:
                    print(f"\nDaten eingegeben für {name}, isin {isin}")
                    current_name = name
                print(".", end="")
                cursor.execute("""INSERT INTO stock_data(
                                    isin,
                                    date,
                                    open,
                                    high,
                                    low,
                                    close,
                                    volume,
                                    dividends,
                                    stock_splits)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (isin, i.strftime('%Y-%m-%d'),
                                                                            row['Open'],
                                                                            row['High'],
                                                                            row['Low'],
                                                                            row['Close'],
                                                                            row['Volume'],
                                                                            row['Dividends'],
                                                                            row['Stock Splits']))

            except sqlite3.Error as e:
                error_msg = ("Aktiendaten konnten nicht eingefügt werden.\n"
                             f"Name: {name}\n"
                             f"ISIN: {isin}\n"
                             f"Error: {str(e)}\n")
                raise RuntimeError(error_msg) from e
    print("\n")
    connection.commit()
    connection.close()


if __name__ == "__main__":

    path = os.path.join("..", "server", "database", "FoxFinanceData.db")

    if os.path.exists(path):
        print("Datenbank vorhanden – Daten werden eingefügt")
    else:
        print("Datenbank nicht vorhanden – Script wird nicht weiter ausgeführt")
        sys.exit(0)

    try:
        insert_stock_datas(path)
        print("Daten wurden komplett eingefügt")

    except Exception as e:
        print(f"Fehler bei der Ausfürunng.\nError:{str(e)}")
