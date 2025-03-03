import sqlite3

from db_executor import DBExecutor

class StockData:
    
    def get_Data(self, input):
             
        db_ex = DBExecutor()

        sql= """SELECT * FROM stocks WHERE isin= ? OR ticker_symbol = ? OR company_name = ?"""
        value = (input,)
        stock_identifiers = db_ex.execute(sql, value).fetchall()
        stock_identifiers = stock_identifiers[0]
        names = db_ex.col_names()
        
        stock_dic = {}
        for i in range (len(stock_identifiers)):
            stock_dic[names[i]]= stock_identifiers[i]
       
        db_ex.close()
       
        return stock_dic
    
    