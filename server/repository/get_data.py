import sqlite3

from db_executor import DBExecutor

class GetData:
    
    def get_single_row(self, table, column, search_term):
             
        db_ex = DBExecutor()

        sql= f"""SELECT * FROM {table} WHERE {column}= ?"""
        value = (search_term,)
        data = db_ex.execute(sql, value).fetchall()
        data = data[0]
        names = db_ex.col_names()
        
        result_dic = {}
        for i in range (len(data)):
            result_dic[names[i]]= data[i]
        
        db_ex.close()
       
        return result_dic
    
    
    
    
class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username:str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)  
    
def authenticate_user(username: str, password: str):
    user = get_user(username)
    
    geht das? user.hashed_password