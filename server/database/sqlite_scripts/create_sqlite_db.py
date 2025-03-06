import os, sys, sqlite3

if os.path.exists("../FoxFinance.db"):
    print("Datenbank bereits vorhanden")
    sys.exit(0)
    
connection = sqlite3.connect("../FoxFinanceData.db")
cursor = connection.cursor()


# customer related:
sql = """CREATE TABLE customers(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            registration_date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
            termination_date TEXT,
            last_login TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE (customer_id, registration_date)        
            )"""
cursor.execute(sql)   
            
sql = """CREATE TABLE authentication(
            customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
            email TEXT UNIQUE NOT NULL,
            phone_number TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            disabled BOOL DEFAULT TRUE
            )"""
cursor.execute(sql)   

sql = """CREATE TABLE customer_adresses(
            customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            street TEXT NOT NULL,
            house_number TEXT NOT NULL,
            zip_code INTEGER NOT NULL,
            city TEXT NOT NULL,
            birthday TEXT NOT NULL,
            FOREIGN KEY (zip_code) REFERENCES zip_codes(zip_code),
            UNIQUE (first_name, last_name, birthday)
            )"""
cursor.execute(sql)

sql = """CREATE TABLE financials(
            customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
            reference_account TEXT UNIQUE NOT NULL,
            balance REAL NOT NULL
            )"""
cursor.execute(sql)

sql = """ CREATE TABLE zip_codes(
            zip_code INTEGER PRIMARY KEY,
            city TEXT NOT NULL)"""
cursor.execute(sql)

# stock related:
sql = """CREATE TABLE stocks(
            isin TEXT PRIMARY KEY,
            ticker_symbol TEXT NOT NULL,
            company_name TEXT)"""
cursor.execute(sql)    

sql = """CREATE TABLE stock_data(
            dataID INTEGER PRIMARY KEY,
            isin TEXT,
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            dividends REAL,
            stock_splits REAL,
            FOREIGN KEY (isin) REFERENCES stocks(isin),
            UNIQUE (isin, date)
            )"""
cursor.execute(sql) 

sql = """CREATE TABLE stock_watch(
            watchlist_id INTEGER PRIMARY KEY,
            customer_id INTERGER,
            isin TEXT, price_per_stock REAL,
            transaction_date TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers
            )"""  
cursor.execute(sql) 

sql = """CREATE TABLE stock_indexes(
            index_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            symbol INTERGER NOT NUll
            )"""
cursor.execute(sql)
            
sql = """ CREATE TABLE index_members(
            isin NOT NULL,
            index_id NOT NULL,
            PRIMARY KEY (isin, index_id),
            FOREIGN KEY (isin) REFERENCES stocks,
            FOREIGN KEY (index_id) REFERENCES stock_indexes
            )"""
cursor.execute(sql)

sql = """ CREATE TABLE transactions(
            transactions_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER
            isin NOT NULL,
            transaction_status_id,
            count INTEGER NOT NULL,
            price_per_stock NOT NULL,
            order_charge_id NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers,
            FOREIGN KEY (isin) REFERENCES stocks,
            FOREIGN KEY (transaction_status_id) REFERENCES transaction_status
            )"""
cursor.execute(sql)

sql = """ CREATE TABLE order_charges(
            order_charge_id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_validation DATE NOT NULL,
            end_validation DATE NOT NULL,
            min_stock_vol DECIAML NOT NULL,
            order_charge_percent DECIMAL NOT NULL,
            kind_of_action
            UNIQUE (start_validation, min_stock_vol)
            )"""
cursor.execute(sql)

sql = """ CREATE TABLE transaction_status(
            transactions_status_id  INTEGER PRIMARY KEY AUTOINCREMENT,
            kind of action TEXT NOT NULL)"""
cursor.execute(sql)


sql = """INSERT INTO stock_indexes(name, symbol) VALUES('DAX', '^GDAXI')"""
cursor.execute(sql)
connection.commit()

sql = """INSERT INTO stock_indexes(name, symbol) VALUES('MDAX', '^MDAXI')"""
cursor.execute(sql)
connection.commit()

sql = """INSERT INTO stock_indexes(name, symbol) VALUES('SDAX', '^SDAXI')"""
cursor.execute(sql)
connection.commit()

sql = """INSERT INTO stock_indexes(name, symbol) VALUES('TecDAX', '^TECDAX')"""
cursor.execute(sql)
connection.commit()

sql = """INSERT INTO stock_indexes(name, symbol) VALUES('EURO STOXX 50', '^STOXX50E')"""
cursor.execute(sql)
connection.commit()


sql = """INSERT INTO transaction_status(kind of action) VALUES('buy')"""
cursor.execute(sql)
sql = """INSERT INTO transaction_status(kind of action) VALUES('sell')"""
cursor.execute(sql)
connection.commit()

connection.close()