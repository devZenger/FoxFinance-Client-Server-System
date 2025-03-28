from .db_executor import DBExecutor

from .insert_repo import key_to_column, key_to_value


def update_one_table(table, update:dict, condition_dic:dict):
    db_ex = DBExecutor()
    db_ex.open_connection_db()

    columns = ""
    for k in update.keys():
        columns=f"{columns}{k}=:{k}, "
    columns = columns[:-2]
    
    condition = ""
    for k in condition_dic.keys():
        condition=f"{condition}{k}=:{k} and "
    condition= condition[:-5]
    
    try:
        sql = f"""UPDATE {table}
                    SET {columns} 
                    WHERE {condition}"""

        values = update
        values.update(condition_dic)
        
        db_ex.execute_and_commit(sql, values)
        
            
    except Exception as e:
        error = f"Fehler bei update_one_table, table:{table}, update:{update}, condition_dic{condition_dic}\nError:{e}"
        raise Exception(error)
        
        