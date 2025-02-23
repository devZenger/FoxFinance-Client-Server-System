import sqlite3

from .db_executor import DBExecutor

class InsertCustomer:
    
    def insert(self, input):
             
        into = DBExecutor()

        sql= """INSERT INTO customers(last_login) VALUES(?)"""
        value = (None,)
        customer_id = into.execute_and_commit(sql, value).lastrowid


        input["customer_id"]=customer_id


        sql = """INSERT INTO customer_adresses VALUES(
                    :customer_id,
                    :first_name,
                    :last_name,
                    :street,
                    :house_number,
                    :zip_code,
                    :city,
                    :birthday)"""
        into.execute_and_commit(sql, input)


        sql = """INSERT INTO authentication VALUES(
                    :customer_id,
                    :email,
                    :phone_number,
                    :password)"""
        into.execute_and_commit(sql, input)


        sql = """INSERT INTO financials VALUES(
                    :customer_id,
                    :reference_account)"""
        into.execute_and_commit(sql, input)


        into.close()
        






if __name__ == "__main__":

    dic = {"first_name": "fdsf", "last_name": "fdsf", "street": "fdsf", "house_number": "fdsfdsf", "zip_code": "fdsfd", "city": "fdfdsf", "birthday": "fdsdsf" }
    start = InsertCustomer()
    start.insert(dic)
