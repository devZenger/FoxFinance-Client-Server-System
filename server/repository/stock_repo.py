import sqlite3

from .db_executor import DBExecutor
from .search_repo import make_dictionary_one_result

# if used main
#from db_executor_for_test import DBExecutor
#from search_repo import make_dictionary_one_result


db_ex = DBExecutor()

def latest_trade_day_entry(search_term):
    
    try:
        sql=f"""SELECT * 
                FROM stock_data 
                WHERE isin = ? 
                ORDER BY date DESC LIMIT 1 """
                
        value = (search_term,)
        datas = db_ex.execute(sql, value).fetchall()
        
        names = db_ex.col_names()
        
        return make_dictionary_one_result(datas[0], names)
    
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

    
    

if __name__ == "__main__":

    print("start")
    table = "stocks"
    column = "isin"
    search_term = "DE0005190003"
    time = "6 months"
    
    answer = latest_trade_day_entry(search_term)
    
    print(" ")
    #for an in answer:
    #    print(an)

    #print(len(answer))
    print(answer)
    
    print(" ")
    #stocks_row = answer["row_result0"]
    #print(stocks_row)