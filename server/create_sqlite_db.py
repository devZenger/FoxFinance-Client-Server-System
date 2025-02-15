import os, sys, sqlite3

if os.path.exists("FoxFinance.db"):
    print("Datenbank bereits vorhanden")
    sys.exit(0)
    
connection = sqlite3.connect("FoxData.db")
cursor = connection.cursor()


sql = """CREATE TABLE customers(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            registration TEXT DEFAULT (CURRENT_TIMESTAMP)
            last_login TEXT DEFAULT (CURRENT_TIMESTAMP)            
            )"""
cursor.execute(sql)   
            
sql = """CREATE TABLE authentication(
            customer_id INTEGER PRIMARY KEY,
            email TEXT
            phone TEXT
            password TEXT,
            FOREIGEN KEY (customer_id) REFEERENCES customers(customer_id),
            UNIQUE (customer_id, email)
            )"""
cursor.execute(sql)   

sql = """CREATE TABLE customer_adresses(
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            street TEXT,
            zip_code INTEGER,
            city TEXT
            birthday TEXT,
            FOREIGEN KEY (customer_id) REFEERENCES customers(customer_id),
            UNDIQUE (customer_id, first_name, last_name, birthday)
            )"""
cursor.execute(sql)

sql = """CREATE TABLE stocks(
            wkn TEXT PRIMARY KEY,
            ticker_symbol TEXT,
            company_name TEXT)"""
cursor.execute(sql)    

sql = """CREATE TABLE stock_data(
            dataID INTEGER PRIMARY KEY,
            wkn TEXT,
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            dividends REAL,
            stock_splits REAL,
            FOREIGN KEY (wkn) REFERENCES stocks(wkn),
            UNIQUE (wkn, date)
            )"""
cursor.execute(sql) 

sql = """CREATE TABLE stock_watch(
            watchlist_id INTEGER PRIMARY KEY,
            customer_id INTERGER,
            wkn TEXT, price_per_stock REAL,
            transaction_date TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers
            )"""  
cursor.execute(sql) 




connection.commit()

connection.close()