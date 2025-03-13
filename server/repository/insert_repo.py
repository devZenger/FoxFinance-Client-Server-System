import sqlite3

from .db_executor import DBExecutor

db_ex = DBExecutor()

def key_to_column(to_form:dict):
    
    key_str = ""
    for k in to_form.keys():
        key_str=f"{key_str}{k},"
    
    return key_str[:-1]

def key_to_value(to_form:dict):
    
    key_str = ""
    for k in to_form.keys():
        key_str=f"{key_str}:{k},"
    
    return key_str[:-1]


def insert_one_table(table, insert:dict):
    
    try:
        db_ex.open_connection_db()
        
        key_column = key_to_column(insert)
        key_value = key_to_value(insert)
        
        sql=f"""INSERT INTO {table} ({key_column}) VALUES({key_value})"""
        execute_id = db_ex.execute_and_commit(sql, insert).lastrowid

        return execute_id
        
    except Exception as e:
        print(f"postion: insert_one_tabe, Error: {e}")
        raise Exception(e)
    
    finally:
        db_ex.close
        




if __name__ == "__main__":

    print("start")
    input= {
        "customer_id":1,
        "isin": "DE0005190003",
        "transaction_status_id": 1,
        "count": 20,
        "price_per_stock": 86,
        "order_charge_id": 6  
    }
    
    
    
    answer = insert_one_table("transactions", input)
    
    print(answer)
    print("juhuu")