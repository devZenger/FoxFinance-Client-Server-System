import os
import sys
import sqlite3
from passlib.context import CryptContext

path_csv = os.path.join("..", "server", "database", "sqlite_scripts", "customer_adresses.csv")
# d = open("customer_adresses.csv", encoding='utf-8')

print(path_csv)

try:
    d = open(path_csv, encoding='utf-8')
    print("opened file")

except:
    print("Datei nicht geöffnet")
    sys.exit(0)

print(d.readline())

tx = d.read()
d.close()

line_list = tx.split("\n")

path = os.path.join("..", "server", "database", "FoxFinanceData.db")

try:
    connection = sqlite3.connect(path)
    print("Verbunden")
except:
    print("Fehler in der Verbundung")

cursor = connection.cursor()


password = "12345+-QWert"
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
password_hash = password_context.hash(password)


var = 0

for line in line_list:
    if line:

        try:
            var = var + 1
            regi_date = f"2020-01-01 00:00:{var}"

            sql = "INSERT INTO customers(registration_date) VALUES(?)"
            cursor.execute(sql, (regi_date,))

            customer_id = cursor.lastrowid

            row_list = line.split(";")

            new_user = {"customer_id": customer_id,
                        "last_name": row_list[0],
                        "first_name": row_list[1],
                        "street": row_list[2],
                        "house_number": row_list[3],
                        "city": row_list[4],
                        "zip_code": row_list[5],
                        "phone_number": row_list[6],
                        "email": row_list[7],
                        "birthday": row_list[8],
                        "reference_account": row_list[9],
                        "password": password_hash,
                        "disabled": False,
                        "balance": 30000}

            print(new_user)

            sql = """INSERT INTO customer_adresses(
                customer_id,
                first_name,
                last_name,
                street,
                house_number,
                zip_code,
                city,
                birthday) VALUES(
                :customer_id,
                :first_name,
                :last_name,
                :street,
                :house_number,
                :zip_code,
                :city,
                :birthday)"""
            cursor.execute(sql, new_user)

            sql = """INSERT INTO authentication(
                customer_id,
                email,
                phone_number,
                password,
                disabled) VALUES(
                :customer_id,
                :email,
                :phone_number,
                :password,
                :disabled)"""
            cursor.execute(sql, new_user)

            sql = """INSERT INTO financials VALUES(
                        :customer_id,
                        :reference_account,
                        :balance)"""
            cursor.execute(sql, new_user)
            connection.commit()

        except:
            print("not insert")

connection.close()
