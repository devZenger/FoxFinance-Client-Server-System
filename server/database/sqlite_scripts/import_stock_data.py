import yfinance as yf
import os, sys, sqlite3

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
        historical_data = ticker_data.history(period='5d')
    except:
        print("Fehler konnte keine Daten zum Ticker Symbol finden")
        
    for i, row in historical_data.iterrows():
        wrote = False
        try:
            cursor.execute("INSERT INTO stock_data(isin, date, open, high, low, close, volume, dividends, stock_splits) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (isin, i.strftime('%Y-%m-%d'), row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Dividends'], row['Stock Splits']))
            connection.commit()
            if wrote == False:
                print(f"Daten eingegeben für {name}, isin {isin}")
                wrote = True
        except:
            print(f"Fehler Daten von {name} isin: {isin} konnte nicht eingetragen werden")

connection.commit()
connection.close()

