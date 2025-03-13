import sqlite3

from .db_executor import DBExecutor
from .search_repo import make_dictionary_one_result, make_dictionary

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
        raise ValueError(e)
    
    finally:
        db_ex.close()
        return dic


def search_past_balance_transactions(customer_id, search_start, search_end):
    
    db_ex.open_connection_db()
    
    try: 
        sql="""SELECT
                    bt.balance_transaction_id,
                    bt.balance_transaction_date,
                    btt.type_of_action,
                    bt.balance_sum,
					bt.bank_account
                    FROM (
                        SELECT * 
                        FROM balance_transactions AS bt
                        WHERE bt.customer_id = ? 
                            AND bt.balance_transaction_date >= ?
                            AND bt.balance_transaction_date <= ?
                        ORDER BY bt.balance_transaction_date ASC
                    ) AS bt
                    LEFT JOIN (
                        SELECT btt.balance_transaction_type_id, btt.type_of_action
                        FROM balance_transactions_type AS btt
                        )AS btt
                        ON bt.balance_transaction_type_id = btt.balance_transaction_type_id"""
        

        value = (customer_id, search_start, search_end,)
        datas = db_ex.execute(sql, value).fetchall()
            
        names = db_ex.col_names()
        
        result = make_dictionary(datas, names)

        print(f"result ist : {result}")
        
        return result

    except Exception as e:
        print(f"postion: search_past_balance_transactions, Error: {e}")
        raise e

    finally:
        db_ex.close()






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