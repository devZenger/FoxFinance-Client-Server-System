import sqlite3

from .db_executor import DBExecutor
from .search_repo import make_dictionary_one_result

db_ex = DBExecutor()

def latest_trade_day_entry(search_term):
    
    try:
        sql=f"""SELECT * 
                FROM stock_data 
                WHERE isin = ? 
                ORDER BY date DESC LIMIT 1"""
                
        value = (search_term,)
        datas = db_ex.execute(sql, value).fetchall()
        print("datas:")
        print(datas)
        names = db_ex.col_names()
        
        print("data0")
        print(datas[0])
        result= make_dictionary_one_result(datas[0], names)
        print("latest_trade return:")
        print(result)
        return result
        
    except:
        print("debug nicht gefunden")
        return None

def trade_day_by_period(search_term, time):
    
    try:
        sql=f"""SELECT * 
                FROM stock_data 
                WHERE isin = ? AND date <= DATE('now', '-{time}') 
                ORDER BY date DESC LIMIT 1"""
                
        value = (search_term,)
        datas = db_ex.execute(sql, value).fetchall()
        names = db_ex.col_names()
        
        
        return make_dictionary_one_result(datas[0], names)
    
    except:
        print("debug nicht gefunden")
        return None

    


def all_stocks_by_customer(customer_id, isin):
    
    try: 
        sql="""SELECT
                    COALESCE((SELECT SUM(count) 
                        FROM transactions
                        WHERE customer_id = ? AND isin = ? AND transaction_type_id = 1), 0) -
                    COALESCE((SELECT SUM(count) 
                        FROM transactions
                        WHERE customer_id = ? AND isin = ? AND transaction_type_id = 2), 0)
                AS DIFFERENCE"""
        
        value = (customer_id,isin, customer_id,isin,)
        datas = db_ex.execute(sql, value).fetchall()
        
        return datas[0][0]
        
    except:
        print("Fehler")






if __name__ == "__main__":

    print("start")
    table = "stocks"
    
    isin = "DE0005190003"
    customer_id = 2
    
    answer = select_all_stock_by_customer(customer_id, isin)
    
    print(" ")
    #for an in answer:
    #    print(an)

    #print(len(answer))
    print(answer)
    
    print(" ")
    #stocks_row = answer["row_result0"]
    #print(stocks_row)
    
    
#"""SELECT
#                    (SELECT SUM(count) 
#                    FROM transactions
#                    WHERE customer_id = ? AND isin = ? AND transaction_type_id = 1) -
#                    (SELECT SUM(count) 
#                    FROM transactions
#                    WHERE customer_id = ? AND isin = ? AND transaction_type_id = 2)
#                AS DIFFERENCE"""
#                
                
                
                
#                """SELECT SUM(count) 
#                FROM transactions
#                WHERE customer_id = ? AND isin = ? AND transaction_type_id = 1"""