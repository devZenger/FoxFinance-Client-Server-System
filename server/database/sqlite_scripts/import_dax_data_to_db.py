import os
import sys
import sqlite3


def insert_dax_members(path):

    path_csv = os.path.join("..", "server", "database", "sqlite_scripts", "dax.csv")

    try:
        d = open(path_csv, encoding='utf-8')

    except FileNotFoundError as e:
        error_msg = ("Die 'dax.csv' konnte nicht geöffnet werden\n"
                     f"Pfad: {path_csv}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e

    d.readline()
    tx = d.read()
    d.close()

    li = tx.split("\n")

    try:
        connection = sqlite3.connect(path)

    except sqlite3.Error as e:
        error_msg = ("Verbindungsprobleme mit der Datenbank\n"
                     f"Pfad: {path}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e

    cursor = connection.cursor()

    try:
        sql = "SELECT index_id FROM stock_indexes WHERE name = 'DAX'"
        cursor.execute(sql)

        dax_id_tulp = cursor.fetchone()

        dax_id = dax_id_tulp[0]

    except sqlite3.Error as e:
        error_msg = ("Konnte 'dax_id' nicht auslesen.\n"
                     f"SQL: {sql}\n"
                     f"Error: {str(e)}\n")
        connection.close()
        raise RuntimeError(error_msg) from e
    try:
        for zeile in li:
            if zeile:
                ds = zeile.split(",")
                sql = f"INSERT INTO stocks (isin, ticker_symbol, company_name) VALUES('{ds[0]}', '{ds[1]}', '{ds[2]}')"
                cursor.execute(sql)
                connection.commit()
                sql = f"INSERT INTO index_members (isin, index_id) VALUES('{ds[0]}', '{dax_id}')"
                cursor.execute(sql)
                connection.commit()

                print(f"{ds[0]} {ds[1]} {ds[2]}")

    except sqlite3.Error as e:
        error_msg = ("Ausführungprobleme beim Einfügen von Dax Unternehmen.\n"
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
        insert_dax_members(path)
        print("Daten wurden komplett eingefügt")

    except Exception as e:
        print(f"Fehler bei der Ausfürunng.\n Error:{str(e)}")
