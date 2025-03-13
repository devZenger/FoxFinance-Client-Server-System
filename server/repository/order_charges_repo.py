from .db_executor import DBExecutor

from .search_repo import make_dictionary_one_result

db_ex = DBExecutor()


def search_order_charges(volumn, date):
    
    try:
        db_ex.open_connection_db()
        
        sql=f"""SELECT * 
                FROM order_charges
                WHERE start_validation <= ? AND ? <= end_validation AND ? >= min_volumn 
                ORDER BY min_volumn DESC
                LIMIT 1"""
        value = (date, date, volumn)
        datas = db_ex.execute(sql, value).fetchall()
                
        names = db_ex.col_names()
        
        result = make_dictionary_one_result(datas[0], names)
    
    except Exception as e:
        print(f"position: search_order_charges, Error: {e}")
        result = "Kein Eintrag gefunden, Error: {e}"
    
    finally:
        db_ex.close()
        return result





if __name__ == "__main__":

    print("start")
    table = "stocks"
    column = "isin"
    
    search_term = "DE0005190003"
    time = "6 months"
    
    date="2021-5-21"
    volumn=324
    
    answer = search_order_charges(volumn, date)
    
    print(answer)