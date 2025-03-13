import sqlite3

from .db_executor import DBExecutor
from .search_repo import make_dictionary_one_result

db_ex = DBExecutor()

def latest_trade_day_entry(search_term):
    
    try:
        
        db_ex.open_connection_db()
        
        sql=f"""SELECT * 
                FROM stock_data 
                WHERE isin = ? 
                ORDER BY date DESC LIMIT 1"""
                
        value = (search_term,)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()

        result= make_dictionary_one_result(datas[0], names)


        
    except Exception as e:
        print(f"position: latest_trade_day_entry, Error: {e}")
        result = "Kein Eintrag gefunden, Error: {e}"
    
    finally:
        db_ex.close()
        return result

def trade_day_by_period(search_term, time):
    
    try:
        
        db_ex.open_connection_db()
        
        sql=f"""SELECT * 
                FROM stock_data 
                WHERE isin = ? AND date <= DATE('now', '-{time}') 
                ORDER BY date DESC LIMIT 1"""
                
        value = (search_term,)
        datas = db_ex.execute(sql, value).fetchall()
        names = db_ex.col_names()
        
        
        result = make_dictionary_one_result(datas[0], names)
    
    except Exception as e:
        print(f"position: trade_day_by_period, Error: {e}")
        result = "Kein Eintrag gefunden, Error: {e}"
    
    finally:
        db_ex.close()
        return result

    


def all_stocks_by_customer(customer_id, isin):
    
    try:
        db_ex.open_connection_db()
        
        sql="""SELECT
                    COALESCE((SELECT SUM(amount) 
                        FROM transactions
                        WHERE customer_id = ? AND isin = ? AND transaction_type_id = 1), 0) -
                    COALESCE((SELECT SUM(amount) 
                        FROM transactions
                        WHERE customer_id = ? AND isin = ? AND transaction_type_id = 2), 0)
                AS DIFFERENCE"""
        
        value = (customer_id,isin, customer_id,isin,)
        datas = db_ex.execute(sql, value).fetchall()
        
        result = datas[0][0]
        
    except Exception as e:
        print(f"postion: all_stock_by_customer, Error: {e}")
        result = "Kein Eintrag gefunden, Error: {e}"

    finally:
        db_ex.close()
        return result






    
