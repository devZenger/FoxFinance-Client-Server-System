import os, sys, sqlite3


path = os.path.join("..", "server", "database", "FoxFinanceData.db")

print(path)

if os.path.exists(path):
    print("Datenbank bereits vorhanden")

else:
    print("Datenbank nicht vorhanden")
    
connection = sqlite3.connect(path)
cursor = connection.cursor()


sql = """CREATE TABLE watchlist(
            wl_nr INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            isin TEXT,
            price DECIMAL,
            date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
            UNIQUE (customer_id, isin),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )"""
cursor.execute(sql)

connection.commit()



connection.close()