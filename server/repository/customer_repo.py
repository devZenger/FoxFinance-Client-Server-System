import sqlite3

from .db_executor import DBExecutor


    
def insert_customer(input):
            
    db_ex = DBExecutor()
    db_ex.open_connection_db()
    
    try:
        db_ex.start_transcation()

        sql= """INSERT INTO customers(last_login) VALUES(?)"""
        value = (None,)
        customer_id = db_ex.execute(sql, value).lastrowid
        print(customer_id)
        input["customer_id"]=customer_id
        input["disabled"]=False
        input["bank_account"]=input["reference_account"]
        input["balance_transaction_type_id"]= 1
        input["usage"]="Depoteröffnung"
        
        print(input)
        

        sql = """INSERT INTO customer_adresses VALUES(
                    :customer_id,
                    :first_name,
                    :last_name,
                    :street,
                    :house_number,
                    :zip_code,
                    :city,
                    :birthday)"""
        db_ex.execute(sql, input)

        sql = """INSERT INTO authentication VALUES(
                    :customer_id,
                    :email,
                    :phone_number,
                    :password,
                    :disabled)"""
        db_ex.execute(sql, input)

        sql = """INSERT INTO financials VALUES(
                    :customer_id,
                    :reference_account)"""
        db_ex.execute(sql, input)
        
        sql = """INSERT INTO balance_transactions
                    (customer_id,
                    bank_account,
                    balance_sum,
                    balance_transaction_type_id,
                    usage)    
                    VALUES(
                    :customer_id,
                    :bank_account,
                    :balance_sum,
                    :balance_transaction_type_id,
                    :usage)"""
        db_ex.execute(sql, input)
        
        db_ex.connection_commit()


        
        
    
    except Exception as e:
        db_ex.rollback()
        print(e)
        raise f"Error: {e}"
    
    finally:
        db_ex.close()
      
       
            


        






if __name__ == "__main__":

    dic = {'last_name': 'zoe', 'first_name': 'zoe', 'street': 'zoe', 'house_number': 'zoe', 'zip_code': 'zoe', 'city': 'zoe', 'birthday': 'zoe', 'email': 'zoe', 'phone_number': 'zoe', 'reference_account': 'zoe', 'balance_sum': '666666666666666', 'password': '$2b$12$D90SkgxkQvGJz5cWW1.bue2nUiPifhP/yMMhPDU8RujSymMjJDfZC', 'customer_id': 1, 'disabled': False, 'bank_account': 'zoe', 'balance_transaction_type_id': 1, 'usage': 'Depoteröffnung'}
    test = insert_customer(dic)
    
