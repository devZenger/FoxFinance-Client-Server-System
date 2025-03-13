import sqlite3

from .db_executor import DBExecutor
from .search_repo import make_dictionary_one_result

db_ex = DBExecutor()

def customer_balance(customer_id):
    
    try:
        db_ex.open_connection_db()
        
        sql=f"""SELECT 
                    COALESCE((SELECT SUM(isin, amount)
                                FROM balance_transactions 
                                WHERE customer_id = ? AND balance_transaction_type_id = 1), 0) -
                    COALESCE((SELECT SUM(isin, amount)
                                FROM balance_transactions 
                                WHERE customer_id = ? AND balance_transaction_type_id = 2), 0)
                AS actual_depot"""
                
        value = (customer_id, customer_id, customer_id, customer_id,)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()
        
        dic = {}
        dic[names[0]] = datas[0][0] 
        
        return dic
        
    except:
        print(f"position: customer_balance, Error {e}")
        return None
    
    finally:
        db_ex.close()