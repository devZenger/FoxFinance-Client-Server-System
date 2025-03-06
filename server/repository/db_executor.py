import sqlite3
import os, sys


class DBExecutor:
    def __init__(self):
        self.path= "../server/database/FoxFinanceData.db"
        self.cursor = None
        self.connection = None
        
        if os.path.exists(self.path):
            print("Datenbank vorhanden")
        else:
            print("keine Datenbank")
        
        self.path1= "../server/database/FoxFinanceData.db"
        
        if os.path.exists(self.path1):
            print("Datenbank1 vorhanden")
        else:
            print("keine Datenbank")
        
        self.path2= "/../server/database/FoxFinanceData.db"
        
        if os.path.exists(self.path2):
            print("Datenbank2 vorhanden")
        else:
            print("keine Datenbank")
        

            
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
            print("Mit Datenbank verbunden")
        except sqlite3.Error as e:
            print(f"Verbindungsprobleme: {str(e)}")
            raise Exception(f"Verbidungsprobleme: {str(e)}")

  
    def execute(self, sql, value):
        try:
            self.cursor.execute(sql, value)
        except sqlite3.Error as e:
            print(f"Ausführungsprobleme: {str(e)}")
            raise Exception(f"Ausführungsprobleme: {str(e)}")
        
        return self.cursor

     
    def execute_and_commit(self, sql, value):
        try:
            self.cursor.execute(sql, value)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Ausführungsprobleme: {str(e)}")
            raise Exception(f"Ausführungsprobleme: {str(e)}")
        
        return self.cursor
    
    
    def execute_and_commit_just_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Ausführungsprobleme: {str(e)}")
            raise Exception(f"Ausführungsprobleme: {str(e)}")
        
        return self.cursor
    
    
        
    def col_names(self):
        col_name=[]
        names = self.cursor.description
        for name in names:
            col_name.append(name[0])
        
        return col_name
            
        
    
    def close(self):
        self.connection.close()

    

    