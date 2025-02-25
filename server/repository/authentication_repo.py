import sqlite3

from .db_executor import DBExecutor

class AuthData:
    
    def get_data(self, input):
             
        db_ex = DBExecutor()

        sql= """SELECT * FROM authentication WHERE email= ?"""
        value = (input,)
        data = db_ex.execute(sql, value).fetchall()

        
        
        db_ex.close()