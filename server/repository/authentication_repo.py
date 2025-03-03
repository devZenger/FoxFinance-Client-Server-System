import sqlite3

from .db_executor import DBExecutor

    
def get_auth_datas(email):
            
    db_ex = DBExecutor()

    sql= """SELECT * FROM authentication WHERE email= ?"""
    value = (email,)
    data = db_ex.execute(sql, value).fetchall()
    data = data[0]
    names = db_ex.col_names()
    
    auth_dic = {}
    for i in range (len(data)):
        auth_dic[names[i]]= data[i]
    
    db_ex.close()
    
    print(auth_dic)
    
    return auth_dic


def insert_login_time(customer_id):
    
    db_ex = DBExecutor()
    sql= f"""UPDATE customers SET last_login = CURRENT_TIMESTAMP WHERE customer_id = '{customer_id}'"""
    db_ex.execute_and_commit_just_sql(sql)
    db_ex.close()



