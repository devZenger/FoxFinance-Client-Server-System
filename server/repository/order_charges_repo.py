from .db_executor import DBExecutor

from .search_repo import make_dictionary_one_result

db_ex = DBExecutor()


def search_order_charges(volumn, date):
    
    try: 
        sql=f"""SELECT * 
                FROM order_charges
                WHERE start_validation <= ? AND ? <= end_validation AND ? >= min_volumn 
                ORDER BY min_volumn DESC
                LIMIT 1"""
        value = (date, date, volumn)
        datas = db_ex.execute(sql, value).fetchall()
        
        print(datas)
        
        names = db_ex.col_names()
        
        return make_dictionary_one_result(datas[0], names)
    
    except:
        print("debug nicht gefunden")





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