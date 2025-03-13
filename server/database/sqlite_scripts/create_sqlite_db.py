import os, sys, sqlite3


path = os.path.join("..", "server", "database", "FoxFinanceData.db")

print(path)

if os.path.exists(path):
    print("Datenbank bereits vorhanden")
    sys.exit(0)
else:
    print("Datenbank nicht vorhanden")
    
connection = sqlite3.connect(path)
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
            reference_account TEXT UNIQUE NOT NULL
            )"""
cursor.execute(sql)

sql = """ CREATE TABLE zip_codes(
            zip_code INTEGER PRIMARY KEY,
            city TEXT NOT NULL)"""
cursor.execute(sql)

# balance related:
sql = """CREATE TABLE balance_transactions(
            balance_transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            bank_account TEXT NOT NULL,
            balance_sum REAL NOT NULL,
            balance_transaction_type_id INTEGER NOT NULL,
            usage TEXT,
            balance_transaction_date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customers,
            FOREIGN KEY (balance_transaction_type_id) REFERENCES balance_transactions_type)"""
cursor.execute(sql)

sql = """CREATE TABLE balance_transactions_type(
            balance_transaction_type_id INTEGER PRIMARY KEY,
            type_of_action TEST NOT NULL)"""
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
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            isin NOT NULL,
            transaction_type_id,
            amount INTEGER NOT NULL,
            price_per_stock NOT NULL,
            order_charge_id NOT NULL,
            transaction_date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers,
            FOREIGN KEY (isin) REFERENCES stocks,
            FOREIGN KEY (transaction_type_id) REFERENCES transaction_type,
            FOREIGN KEY (order_charge_id) REFERENCES order_charges
            )"""
cursor.execute(sql)

sql = """ CREATE TABLE order_charges(
            order_charge_id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_validation DATE NOT NULL,
            end_validation DATE NOT NULL,
            min_volumn DECIAML NOT NULL,
            order_charge DECIMAL NOT NULL,
            UNIQUE (start_validation, min_volumn)
            )"""
cursor.execute(sql)

sql = """ CREATE TABLE transaction_type(
            transaction_type_id  INTEGER PRIMARY KEY AUTOINCREMENT,
            kind_of_action TEXT NOT NULL)"""
cursor.execute(sql)


sql = """INSERT INTO stock_indexes(name, symbol) VALUES('DAX', '^GDAXI')"""
cursor.execute(sql)

sql = """INSERT INTO stock_indexes(name, symbol) VALUES('MDAX', '^MDAXI')"""
cursor.execute(sql)


sql = """INSERT INTO stock_indexes(name, symbol) VALUES('SDAX', '^SDAXI')"""
cursor.execute(sql)


sql = """INSERT INTO stock_indexes(name, symbol) VALUES('TecDAX', '^TECDAX')"""
cursor.execute(sql)


sql = """INSERT INTO stock_indexes(name, symbol) VALUES('EURO STOXX 50', '^STOXX50E')"""
cursor.execute(sql)
connection.commit()


sql = """INSERT INTO transaction_type(kind_of_action) VALUES('buy')"""
cursor.execute(sql)
sql = """INSERT INTO transaction_type(kind_of_action) VALUES('sell')"""
cursor.execute(sql)
connection.commit()


sql = """INSERT INTO balance_transactions_type(type_of_action) VALUES('deposit')"""
cursor.execute(sql)

sql = """INSERT INTO balance_transactions_type(type_of_action) VALUES('withdrawal')"""
cursor.execute(sql)

sql = """INSERT INTO balance_transactions_type(type_of_action) VALUES('buy stocks')"""
cursor.execute(sql)

sql = """INSERT INTO balance_transactions_type(type_of_action) VALUES('sell stocks')"""
cursor.execute(sql)


connection.commit()


sql = """INSERT INTO order_charges(
            start_validation,
            end_validation, 
            min_volumn, 
            order_charge 
            ) VALUES(
            '2018-01-01',
            '2020-12-31',
            0,
            0.1)"""
cursor.execute(sql)

sql = """INSERT INTO order_charges(
            start_validation,
            end_validation, 
            min_volumn, 
            order_charge 
            ) VALUES(
            '2018-01-01',
            '2020-12-31',
            1000,
            0.05)"""
cursor.execute(sql)

sql = """INSERT INTO order_charges(
            start_validation,
            end_validation, 
            min_volumn, 
            order_charge 
            ) VALUES(
            '2021-01-01',
            '2023-12-31',
            0,
            0.08)"""
cursor.execute(sql)

sql = """INSERT INTO order_charges(
            start_validation,
            end_validation, 
            min_volumn, 
            order_charge 
            ) VALUES(
            '2021-01-01',
            '2023-12-31',
            800,
            0.06)"""
cursor.execute(sql)

sql = """INSERT INTO order_charges(
            start_validation,
            end_validation, 
            min_volumn, 
            order_charge 
            ) VALUES(
            '2024-01-01',
            '2025-12-31',
            0,
            0.07)"""
cursor.execute(sql)

sql = """INSERT INTO order_charges(
            start_validation,
            end_validation, 
            min_volumn, 
            order_charge 
            ) VALUES(
            '2024-01-01',
            '2025-12-31',
            600,
            0.05)"""
cursor.execute(sql)
connection.commit()



connection.close()