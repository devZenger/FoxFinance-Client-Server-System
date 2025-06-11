import os
import sys
import sqlite3

from .insert_base_data_to_db import insert_datas
from .import_customer_data_to_db import insert_customers
from .import_dax_data_to_db import insert_dax_members
from .import_stock_data_to_db import insert_stock_datas
from .max_mustermann import insert_mustermann, email, password


def create_tables(path):

    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()

        # customer related:
        sql = """CREATE TABLE customers(
                    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,

                    email TEXT UNIQUE NOT NULL,
                    phone_number TEXT UNIQUE NOT NULL,
                    birthday TEXT NOT NULL,

                    registration_date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    termination_date TEXT,
                    disabled BOOL DEFAULT TRUE,

                    last_login TEXT DEFAULT CURRENT_TIMESTAMP,
                    client_ip TEXT NOT NULL,
                    UNIQUE (customer_id, registration_date),
                    UNIQUE (first_name, last_name, birthday)
                    )"""
        cursor.execute(sql)

        sql = """CREATE TABLE customer_addresses(
                    customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
                    street TEXT NOT NULL,
                    house_number TEXT NOT NULL,
                    zip_code INTEGER NOT NULL,
                    city TEXT NOT NULL
                    )"""
        cursor.execute(sql)

        sql = """CREATE TABLE financials(
                    customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
                    reference_account TEXT UNIQUE NOT NULL
                    )"""
        cursor.execute(sql)

        sql = """CREATE TABLE authentication(
                    customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
                    password TEXT NOT NULL
                    )"""
        cursor.execute(sql)

        # validation:
        sql = """CREATE TABLE validation(
                    customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
                    validation_number INTEGER NOT NULL,
                    date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
                    )"""
        cursor.execute(sql)

        sql = """CREATE TRIGGER update_date_trigger
                    AFTER UPDATE OF validation_number ON validation
                    FOR EACH ROW
                    BEGIN
                        UPDATE validation
                        SET date = CURRENT_TIMESTAMP
                        WHERE customer_id = NEW.customer_id;
                END"""

        cursor.execute(sql)

        # financial related:
        sql = """CREATE TABLE financial_transactions(
                    financial_transfer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER NOT NULL,
                    bank_account TEXT NOT NULL,
                    fin_amount REAL NOT NULL,
                    fin_transaction_type_id INTEGER NOT NULL,
                    usage TEXT,
                    fin_transaction_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (customer_id) REFERENCES customers,
                    FOREIGN KEY (fin_transaction_type_id) REFERENCES fin_transaction_types)"""
        cursor.execute(sql)

        sql = """CREATE TABLE fin_transaction_types(
                    fin_transaction_type_id INTEGER PRIMARY KEY,
                    fin_transaction_type TEXT NOT NULL)"""
        cursor.execute(sql)

        # stock related:
        sql = """CREATE TABLE stocks(
                    isin TEXT PRIMARY KEY,
                    ticker_symbol TEXT NOT NULL,
                    company_name TEXT NOT NULL)"""
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

        sql = """CREATE TABLE watchlist(
                    wl_nr INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    isin TEXT,
                    price REAL,
                    date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    UNIQUE (customer_id, isin),
                    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
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
                    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('buy', 'sell')),
                    amount INTEGER NOT NULL,
                    price_per_stock NOT NULL,
                    order_charge_id NOT NULL,
                    transaction_date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES customers,
                    FOREIGN KEY (isin) REFERENCES stocks,
                    FOREIGN KEY (order_charge_id) REFERENCES order_charges
                    )"""
        cursor.execute(sql)

        sql = """ CREATE TABLE order_charges(
                    order_charge_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    start_validation DATE NOT NULL,
                    end_validation DATE NOT NULL,
                    min_volumn REAL NOT NULL,
                    order_charge REAL NOT NULL,
                    UNIQUE (start_validation, min_volumn)
                    )"""
        cursor.execute(sql)

        connection.commit()

    except sqlite3.Error as e:
        error_msg = ("Fehler beim Erstellen der Tabellen.\n"
                     f"SQL: {sql}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e

    finally:
        connection.close()


def choice(question: str, function, path):
    feedback = False
    while feedback is False:
        user_input = input(f"\n{question} (Ja/Nein): ")
        user_input = user_input.lower()
        if user_input == "ja" or user_input == "j":
            function(path)
            feedback = True
        elif user_input == "nein" or user_input == "n":
            feedback = True
            return True
        else:
            print("Ungültige Eingabe, bitte wiederholen.")


def create_db(path):

    try:
        create_tables(path)
        insert_datas(path)

        choice("Max Mustermann anlegen", insert_mustermann, path)
        choice("Kundendaten einfügen", insert_customers, path)

        insert_dax_members(path)
        insert_stock_datas(path)

        return "Datenbank Einsatzbereit", email, password

    except Exception as e:
        error_msg = ("Fehler bei 'create_db'.\n"
                     f"Error: {e}\n")
        raise RuntimeError(error_msg) from e


if __name__ == "__main__":

    path = os.path.join("..", "server", "database", "FoxFinanceData.db")

    if os.path.exists(path):
        print("Datenbank bereits vorhanden – Script wird nicht weiter ausgeführt")
        sys.exit(0)
    else:
        print("Datenbank nicht vorhanden – Script ausgeführt")

    try:
        answer = choice("Nur Tabellen ersellen (bei Nein, auch die Daten)", create_tables, path)
        if answer:
            create_db(path)
            print("Datenbank erstellt, Tabellen eingefügt, Daten eingefügt")
        else:
            print("Datenbank erstellt, Tabellen eingefügt")

    except Exception as e:
        print(f"Fehler bei der Ausfürunng.\n Error:{str(e)}")
