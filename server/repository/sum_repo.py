import sqlite3

from .db_executor import DBExecutor

# if used main
#from db_executor_for_test import DBExecutor
    
def simple_search(table, column, search_term):
            
    db_ex = DBExecutor()
    try:
        sql= f"""SELECT * FROM {table} WHERE {column} LIKE ?"""
        value = (search_term,)
        datas = db_ex.execute(sql, value).fetchall()
        print(datas)
        
        names = db_ex.col_names()
        
        search_result = {}
        row_data = {}
        i = 0
        for data in datas:
            print(f"data: {data}")
            row_data = {}
            for j in range (len(data)):
                row_data[names[j]] = data[j]
                print(f"{j} {data[j]}")
                print("-------")
            
            search_result[f"row_result{i}"]= row_data
            print(f"search {search_result} i = {i}")
            i += 1
        
        
        print (f"search reslut: {search_result}")
            
          
        
        return search_result
    
    except:
        print("debug none")
        return None







if __name__ == "__main__":

    print("start")
    table = "stocks"
    column = "company_name"
    search_term = "%%deutsche%%"
    isin= "DE000519003"
    
    answer = simple_search(table, column, search_term)
    
    print(" ")
    #for an in answer:
     #   print(an)

    print(len(answer))
    print(answer)