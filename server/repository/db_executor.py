import sqlite3

import os, sys

class DBExecutor:
    def __init__(self):
        self.path= "FoxFinanceData.db"
        self.cursor = None
        self.connection = None
        
        if os.path.exists("FoxFinanceData.db"):
                 print("Datenbank bereits vorhanden")
        else:
            print("keine Datenbank")
            
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
            print("verbunden")
        except sqlite3.Error as e:
            print(f"Verbindungsprobleme: {str(e)}")
            raise Exception(f"Verbidungsprobleme: {str(e)}")
        
    def execute_and_commit(self, sql, value):
        
        try:
            self.cursor.execute(sql, value)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Ausführungsprobleme: {str(e)}")
            raise Exception(f"Ausführungsprobleme: {str(e)}")
        
        return self.cursor
    
    def close(self):
        self.connection.close()

    

    