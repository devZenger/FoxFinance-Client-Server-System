import sqlite3

from .db_executor import DBExecutor

class AuthData:
    
    def get_data(self, input):
             
        db_ex = DBExecutor()

        sql= """SELECT * FROM authentication WHERE email= ?"""
        value = (input,)
        data = db_ex.execute(sql, value).fetchall()
        data = data[0]
        names = db_ex.col_names()
        
        auth_dic = {}
        for i in range (len(data)):
            auth_dic[names[i]]= data[i]
        
        db_ex.close()
       
        return auth_dic
    
    

