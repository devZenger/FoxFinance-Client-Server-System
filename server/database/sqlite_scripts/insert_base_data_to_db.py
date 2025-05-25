import os
import sys
import sqlite3


def insert_datas(path):

    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()

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

        sql = """INSERT INTO fin_transaction_types(fin_transaction_type) VALUES('deposit')"""
        cursor.execute(sql)

        sql = """INSERT INTO fin_transaction_types(fin_transaction_type) VALUES('withdrawal')"""
        cursor.execute(sql)

        sql = """INSERT INTO fin_transaction_types(fin_transaction_type) VALUES('buy stocks')"""
        cursor.execute(sql)

        sql = """INSERT INTO fin_transaction_types(fin_transaction_type) VALUES('sell stocks')"""
        cursor.execute(sql)

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

    except sqlite3.Error as e:
        error_msg = ("Ausführungsprobleme beim Einfügen von Basisdaten.\n"
                     f"SQL: {sql}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e

    finally:
        connection.close()


if __name__ == "__main__":

    path = os.path.join("..", "server", "database", "FoxFinanceData.db")

    if os.path.exists(path):
        print("Datenbank vorhanden – Daten werden eingefügt")

    else:
        print("Datenbank nicht vorhanden – Script wird nicht weiter ausgeführt")
        sys.exit(0)
    try:
        insert_datas(path)
        print("Daten wurden eingefügt")

    except Exception as e:
        print(f"Fehler bei der Ausfürunng.\n Error:{str(e)}")
