import sqlite3

from .db_executor import DBExecutor
from .search_repo import make_dictionary_one_result

db_ex = DBExecutor()

def customer_balance(customer_id):
    
    try:
        db_ex.open_connection_db()
        
        sql=f"""SELECT 
                    COALESCE((SELECT SUM(balance_sum)
                                FROM balance_transactions 
                                WHERE customer_id = ? AND balance_transaction_type_id = 1), 0) +
	                COALESCE((SELECT SUM(balance_sum) 
                                FROM balance_transactions 
                                WHERE customer_id = ? AND balance_transaction_type_id = 4), 0) -
	                COALESCE((SELECT SUM(balance_sum) 
                                FROM balance_transactions 
                                WHERE customer_id = ? AND balance_transaction_type_id = 2), 0) -
	                COALESCE((SELECT SUM(balance_sum) 
                                FROM balance_transactions 
                                WHERE customer_id = ? AND balance_transaction_type_id = 3), 0)
                AS actual_balance"""
                
        value = (customer_id, customer_id, customer_id, customer_id,)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()
        
        dic = {}
        dic[names[0]] = datas[0][0] 
        
        
        
    except Exception as e:
        dic = {}
        print(f"Fehler customer balance: {e}")
        raise e
    
    finally:
        db_ex.close()
        return dic




if __name__ == "__main__":

    print("start")
    table = "stocks"
    
    isin = "DE0005190003"
    customer_id = 2
    
    answer = customer_balance(customer_id)
    
    print(" ")
    #for an in answer:
    #    print(an)

    #print(len(answer))
    print(answer)
    
    print(" ")
    #stocks_row = answer["row_result0"]
    #print(stocks_row)
    
    
#"""SELECT