import sqlite3

from .db_executor import DBExecutor

# if used main
#from db_executor_for_test import DBExecutor
 

db_ex = DBExecutor()


def make_dictionary(datas, names):
    
    search_result = {}
    i = 0
    for data in datas:
        print(f"data: {data}")
        row_data = {}
        for j in range (len(data)):
            row_data[names[j]] = data[j]
        
        search_result[f"row_result{i}"]= row_data
        i += 1

    return search_result

def make_dictionary_one_result(datas, names):

    row_data = {}
    for j in range (len(datas)):
        row_data[names[j]] = datas[j]
    
    return row_data
    

   
def simple_search(table, column, search_term):
    
    try:
        db_ex.open_connection_db()
        
        sql= f"""SELECT * FROM {table} WHERE {column} LIKE ?"""
        value = (search_term,)
        datas = db_ex.execute(sql, value).fetchall()
        
        names = db_ex.col_names()
                 
        result= make_dictionary(datas, names)      

        
    except Exception as e:
        print(f"position: search_order_charges, Error: {e}")
        result = f"Kein Eintrag gefunden, Error: {e}"
    
    finally:
        db_ex.close()
        return result


















if __name__ == "__main__":

    print("start")
    table = "stocks"
    column = "isin"
    search_term = "DE0005190003"
    time = "6 months"
    
    answer = simple_search(table, column, search_term)
    
    print(" ")
    #for an in answer:
    #    print(an)

    #print(len(answer))
    print(answer)
    
    print(" ")
    stocks_row = answer["row_result0"]
    print(stocks_row)