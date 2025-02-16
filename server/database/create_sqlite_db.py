import os, sys, sqlite3

if os.path.exists("FoxFinance.db"):
    print("Datenbank bereits vorhanden")
    sys.exit(0)
    
connection = sqlite3.connect("FoxFinanceData.db")
cursor = connection.cursor()


sql = """CREATE TABLE customers(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            registration_date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
            last_login TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
            UNIQUE (customer_id, registration_date)        
            )"""
cursor.execute(sql)   
            
sql = """CREATE TABLE authentication(
            customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
            email TEXT UNIQUE NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
            )"""
cursor.execute(sql)   

sql = """CREATE TABLE customer_adresses(
            customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            street TEXT NOT NULL,
            zip_code INTEGER NOT NULL,
            city TEXT NOT NULL,
            birthday TEXT NOT NULL,
            UNIQUE (first_name, last_name, birthday)
            )"""
cursor.execute(sql)

sql = """CREATE TABLE financials(
            customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
            reference_account TEXT UNIQUE NOT NULL,
            balance REAL NOT NULL
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