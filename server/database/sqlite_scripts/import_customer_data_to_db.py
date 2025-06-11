import os
import sys
import sqlite3
from passlib.context import CryptContext
import base64
from cryptography.fernet import Fernet


# To encrypt bank account
fernet = None


def read_key():
    global fernet
    path = os.path.join("..", "server", "keys", "demo_account.key")
    try:
        with open(path, "rb") as key_file:
            secret_key = key_file.read()

        fernet = Fernet(secret_key)

    except FileNotFoundError as e:
        error_msg = ("'demo_account.key' konnte nicht geöffnet werden.\n"
                     f"Pfad: {path}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e


def bank_account_encode(account: str):
    if fernet is None:
        raise RuntimeError("Fernet wurd nicht initialisiert")

    encode_byte = fernet.encrypt(account.encode('utf-8'))
    encode_str = base64.urlsafe_b64encode(encode_byte).decode('utf-8')
    return encode_str


def insert_customers(path):

    read_key()

    path_csv = os.path.join("..", "server", "database", "sqlite_scripts", "customer_addresses.csv")

    try:
        d = open(path_csv, encoding='utf-8')

    except FileNotFoundError as e:
        error_msg = ("Die 'customer_addresses.csv' konnte nicht geöffnet werden\n"
                     f"Pfad: {path_csv}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e

    print(d.readline())

    tx = d.read()
    d.close()

    line_list = tx.split("\n")

    try:
        connection = sqlite3.connect(path)

    except sqlite3.Error as e:
        error_msg = ("Verbindungsprobleme mit der Datenbank\n"
                     f"Pfad: {path}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e

    cursor = connection.cursor()

    # Kundenpasswort
    password = "12345+-QWert"
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    password_hash = password_context.hash(password)

    var = 0

    for line in line_list:
        if line:

            try:
                var = var + 1
                regi_date = f"2020-01-01 00:00:{var}"

                row_list = line.split(";")

                zip_code = int(row_list[5])
                encrypt_bank_account = bank_account_encode(row_list[9])

                new_user = {"registration_date": regi_date,
                            "last_name": row_list[0],
                            "first_name": row_list[1],
                            "street": row_list[2],
                            "house_number": row_list[3],
                            "city": row_list[4],
                            "zip_code": zip_code,
                            "phone_number": row_list[6],
                            "email": row_list[7],
                            "birthday": row_list[8],
                            "reference_account": encrypt_bank_account,
                            "bank_account": encrypt_bank_account,
                            "usage": "Ersteinzahlung",
                            "fin_transaction_type_id": 1,
                            "password": password_hash,
                            "disabled": False,
                            "fin_amount": 30000,
                            "client_ip": "127.0.0.1"}

                sql = """INSERT INTO customers(
                            first_name,
                            last_name,
                            email,
                            phone_number,
                            birthday,
                            registration_date,
                            disabled,
                            client_ip)
                        VALUES(
                            :first_name,
                            :last_name,
                            :email,
                            :phone_number,
                            :birthday,
                            :registration_date,
                            :disabled,
                            :client_ip
                        )"""
                cursor.execute(sql, new_user)

                customer_id = cursor.lastrowid

                new_user["customer_id"] = customer_id

                sql = """INSERT INTO customer_addresses(
                            customer_id,
                            street,
                            house_number,
                            zip_code,
                            city)
                        VALUES(
                            :customer_id,
                            :street,
                            :house_number,
                            :zip_code,
                            :city
                        )"""
                cursor.execute(sql, new_user)

                sql = """INSERT INTO authentication(
                            customer_id,
                            password)
                        VALUES(
                            :customer_id,
                            :password
                        )"""
                cursor.execute(sql, new_user)

                sql = """INSERT INTO financials
                        VALUES(
                            :customer_id,
                            :reference_account)"""
                cursor.execute(sql, new_user)

                sql = """INSERT INTO financial_transactions(
                            customer_id,
                            bank_account,
                            fin_amount,
                            fin_transaction_type_id,
                            usage)
                        VALUES (
                            :customer_id,
                            :bank_account,
                            :fin_amount,
                            :fin_transaction_type_id,
                            :usage
                        )"""
                cursor.execute(sql, new_user)
                connection.commit()

                print(f"Kunde: {new_user['last_name']} {new_user['first_name']}")

            except sqlite3.Error as e:
                error_msg = ("Ausführungsprobleme beim Einfügen von Kundendaten.\n"
                             f"'new_user': {new_user}\n"
                             f"SQL: {sql}\n"
                             f"Error: {str(e)}")
                connection.close()
                raise RuntimeError(error_msg) from e

    connection.close()


if __name__ == "__main__":

    path = os.path.join("..", "server", "database", "FoxFinanceData.db")

    if os.path.exists(path):
        print("Datenbank vorhanden – Daten werden eingefügt")
    else:
        print("Datenbank nicht vorhanden – Script wird nicht weiter ausgeführt")
        sys.exit(0)

    try:
        insert_customers(path)
        print("Daten wurden komplett eingefügt")

    except Exception as e:
        print(f"Fehler bei der Ausfürunng.\n Error:{str(e)}")
