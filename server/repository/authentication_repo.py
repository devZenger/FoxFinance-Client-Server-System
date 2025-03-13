import sqlite3

from .db_executor import DBExecutor

db_ex = DBExecutor()
    
def get_auth_datas(email):
            
    try:
        db_ex.open_connection_db()
        
        sql= """SELECT * FROM authentication WHERE email= ?"""
        value = (email,)
        data = db_ex.execute(sql, value).fetchall()
        data = data[0]
        names = db_ex.col_names()
        
        auth_dic = {}
        for i in range (len(data)):
            auth_dic[names[i]]= data[i]
        
        db_ex.close()
        
        print(f"debug ausgabe von auth_dic: {auth_dic}")
        
        return auth_dic
    
    except Exception as e:
        print(f"Position: get_auth_datas, Error: {e}")
        return None
    
    finally:
        db_ex.close()
    


def insert_login_time(customer_id):
    
    try:
        db_ex.open_connection_db()
        sql= f"""UPDATE customers SET last_login = CURRENT_TIMESTAMP WHERE customer_id = '{customer_id}'"""
        db_ex.execute_and_commit_just_sql(sql)
    
    except Exception as e:
        print(f"position: insert_login_time; Error: {e}")
    
    finally:
        db_ex.close()



