import os
import sys
import sqlite3
from passlib.context import CryptContext
import base64
from cryptography.fernet import Fernet


email = ""
password = ""


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


# Start Insert Mustermann
def insert_mustermann(path):
    global email
    global password

    read_key()

    try:
        connection = sqlite3.connect(path)

    except sqlite3.Error as e:
        error_msg = ("Verbindungsprobleme mit der Datenbank\n"
                     f"Pfad: {path}\n"
                     f"Error: {str(e)}\n")
        raise sqlite3.Error(error_msg) from e

    cursor = connection.cursor()

    password = "12345+-QWert"
    email = "max@mustermann.de"
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    password_hash = password_context.hash(password)

    account_encode = bank_account_encode("MB001002003004005")

    max_mustermann = {"registration_date": "2023-01-01 08:00:00",
                      "last_name": "Mustermann",
                      "first_name": "Max",
                      "street": "Musterstraße",
                      "house_number": 8,
                      "city": "Musterstadt",
                      "zip_code": 66642,
                      "phone_number": "01761235678",
                      "email": email,
                      "birthday": "23.05.1988",
                      "reference_account": account_encode,
                      "bank_account": account_encode,
                      "usage": "Ersteinzahlung",
                      "fin_transaction_type_id": 1,
                      "password": password_hash,
                      "disabled": False,
                      "fin_amount": 100,
                      "client_ip": "127.0.0.1",
                      "fin_transaction_date": "2023-01-01 08:00:01"}
    try:
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
        cursor.execute(sql, max_mustermann)

        customer_id = cursor.lastrowid

        max_mustermann["customer_id"] = customer_id

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
        cursor.execute(sql, max_mustermann)

        sql = """INSERT INTO authentication(
                    customer_id,
                    password)
                VALUES(
                    :customer_id,
                    :password
                )"""
        cursor.execute(sql, max_mustermann)

        sql = """INSERT INTO financials
                VALUES(
                    :customer_id,
                    :reference_account)"""
        cursor.execute(sql, max_mustermann)

        sql = """INSERT INTO financial_transactions(
                    customer_id,
                    bank_account,
                    fin_amount,
                    fin_transaction_type_id,
                    usage,
                    fin_transaction_date)
                VALUES (
                    :customer_id,
                    :bank_account,
                    :fin_amount,
                    :fin_transaction_type_id,
                    :usage,
                    :fin_transaction_date
                )"""
        cursor.execute(sql, max_mustermann)

    except sqlite3.Error as e:
        error_msg = ("Daten von Max Mustermann konnten nicht eingefügt werden.\n"
                     f"SQL: {sql}\n"
                     f"Error: {e}\n")

    # Transactions
    def order_charge(volume: float, date: str):
        sql = """SELECT *
                FROM order_charges
                WHERE start_validation <= ? AND ? <= end_validation AND ? >= min_volumn
                ORDER BY min_volumn DESC
                LIMIT 1"""
        value = (date, date, volume)
        cursor.execute(sql, value)

        datas = cursor.fetchall()
        charge = datas[0][4]
        charge_id = datas[0][0]

        order_charge_total = charge * volume

        return order_charge_total, charge_id

    # Transaction.csv
    path_csv = os.path.join("..", "server", "database", "sqlite_scripts", "mustermann_transactions.csv")

    try:
        d = open(path_csv, encoding='utf-8')

    except FileNotFoundError as e:
        error_msg = ("Die 'mustermann_transactions.csv' konnte nicht geöffnet werden"
                     f"Pfad: {path}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e

    # First CSV line
    d.readline()

    tx = d.read()
    d.close()

    line_list = tx.split("\n")

    for line in line_list:
        if line:
            try:
                row_list = line.split(";")

                new_order = {"customer_id": customer_id,
                             "isin": row_list[0],
                             "transaction_type": row_list[1],
                             "amount": int(row_list[2]),
                             "price_per_stock": float(row_list[3]),
                             "date": row_list[4],
                             "transaction_date": f"{row_list[4]} 10:00:00",
                             "bank_account": account_encode}

                volume = new_order["amount"] * new_order["price_per_stock"]
                order_charge_total, new_order["order_charge_id"] = order_charge(volume, new_order["transaction_date"])

                sql = """INSERT INTO transactions(
                                customer_id,
                                isin,
                                transaction_type,
                                amount,
                                price_per_stock,
                                order_charge_id,
                                transaction_date) VALUES(
                                :customer_id,
                                :isin,
                                :transaction_type,
                                :amount,
                                :price_per_stock,
                                :order_charge_id,
                                :transaction_date
                                )"""
                cursor.execute(sql, new_order)
                transaction_id = cursor.lastrowid

                if new_order["transaction_type"] == "buy":
                    new_order["fin_amount"] = volume + order_charge_total
                    new_order["fin_transaction_type_id"] = 1
                    new_order["fin_transaction_date"] = f"{new_order['date']} 09:00:00"
                    new_order["usage"] = "Einzahlung"

                    sql = """INSERT INTO financial_transactions(
                        customer_id,
                        bank_account,
                        fin_amount,
                        fin_transaction_type_id,
                        fin_transaction_date,
                        usage) VALUES (
                        :customer_id,
                        :bank_account,
                        :fin_amount,
                        :fin_transaction_type_id,
                        :fin_transaction_date,
                        :usage)"""
                    cursor.execute(sql, new_order)

                    new_order["fin_transaction_type_id"] = 3

                else:
                    new_order["fin_amount"] = volume - order_charge_total
                    new_order["fin_transaction_type_id"] = 4

                new_order["usage"] = f"Aktientransaktions Nr.: {transaction_id}"
                new_order["fin_transaction_date"] = f"{new_order['date']} 10:00:00"

                sql = """INSERT INTO financial_transactions(
                        customer_id,
                        bank_account,
                        fin_amount,
                        fin_transaction_type_id,
                        fin_transaction_date,
                        usage) VALUES (
                        :customer_id,
                        :bank_account,
                        :fin_amount,
                        :fin_transaction_type_id,
                        :fin_transaction_date,
                        :usage)"""
                cursor.execute(sql, new_order)

                if new_order["transaction_type"] == "sell":
                    new_order["fin_transaction_type_id"] = 2
                    new_order["fin_transaction_date"] = f"{new_order['date']} 11:00:00"
                    new_order["usage"] = "Auszahlung"

                    sql = """INSERT INTO financial_transactions(
                        customer_id,
                        bank_account,
                        fin_amount,
                        fin_transaction_type_id,
                        fin_transaction_date,
                        usage) VALUES (
                        :customer_id,
                        :bank_account,
                        :fin_amount,
                        :fin_transaction_type_id,
                        :fin_transaction_date,
                        :usage)"""
                    cursor.execute(sql, new_order)

                connection.commit()

            except Exception as e:
                print("Fehler", str(e))

    connection.close()


if __name__ == "__main__":

    path = os.path.join("..", "server", "database", "FoxFinanceData.db")

    if os.path.exists(path):
        print("Datenbank vorhanden – Daten werden eingefügt")
    else:
        print("Datenbank nicht vorhanden – Script wird nicht weiter ausgeführt")
        sys.exit(0)

    try:
        insert_mustermann(path)
        print("Daten wurden komplett eingefügt")

    except Exception as e:
        print(f"Fehler bei der Ausfürunng.\n Error:{str(e)}")
