import sqlite3

from .db_executor import DBExecutor

class InsertCustomer:
    
    def insert(self, input):
             
        db_ex = DBExecutor()

        sql= """INSERT INTO customers(last_login) VALUES(?)"""
        value = (None,)
        customer_id = db_ex.execute_and_commit(sql, value).lastrowid

        input["customer_id"]=customer_id
        input["disabled"]=False
        


        sql = """INSERT INTO customer_adresses VALUES(
                    :customer_id,
                    :first_name,
                    :last_name,
                    :street,
                    :house_number,
                    :zip_code,
                    :birthday)"""
        db_ex.execute_and_commit(sql, input)


        sql = """INSERT INTO authentication VALUES(
                    :customer_id,
                    :email,
                    :phone_number,
                    :password,
                    :disabled)"""
        db_ex.execute_and_commit(sql, input)


        sql = """INSERT INTO financials VALUES(
                    :customer_id,
                    :reference_account,
                    :balance)"""
        db_ex.execute_and_commit(sql, input)

        db_ex.close()
        






if __name__ == "__main__":

    dic = {"first_name": "fdsf", "last_name": "fdsf", "street": "fdsf", "house_number": "fdsfdsf", "zip_code": "fdsfd", "city": "fdfdsf", "birthday": "fdsdsf" }
    start = InsertCustomer()
    start.insert(dic)
