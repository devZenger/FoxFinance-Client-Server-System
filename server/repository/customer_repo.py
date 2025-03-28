import sqlite3

from .db_executor import DBExecutor


    
def insert_customer(input):
            
    db_ex = DBExecutor()
    db_ex.open_connection_db()
    
    try:
        db_ex.start_transcation()

        input["disabled"]=False
        input["bank_account"]=input["reference_account"]
        input["fin_transaction_type_id"]= 1
        input["usage"]="Depoteröffnung"
        
        sql= """INSERT INTO customers(
                    first_name,
                    last_name,
                    email,
                    phone_number,
                    birthday)
                    VALUES(

                    :first_name,
                    :last_name,
                    :email,
                    :phone_number,
                    :birthday
            )"""
        customer_id = db_ex.execute(sql, input).lastrowid
        input["customer_id"]=customer_id
        
        sql = """INSERT INTO customer_adresses VALUES(
                    :customer_id,
                    :street,
                    :house_number,
                    :zip_code,
                    :city)"""
        db_ex.execute(sql, input)

        sql = """INSERT INTO authentication VALUES(
                    :customer_id,
                    :password)"""
        db_ex.execute(sql, input)

        sql = """INSERT INTO financials VALUES(
                    :customer_id,
                    :reference_account)"""
        db_ex.execute(sql, input)
        
        sql = """INSERT INTO financial_transactions
                    (customer_id,
                    bank_account,
                    fin_amount,
                    fin_transaction_type_id,
                    usage)    
                    VALUES(
                    :customer_id,
                    :bank_account,
                    :fin_amount,
                    :fin_transaction_type_id,
                    :usage)"""
        db_ex.execute(sql, input)
        
        db_ex.connection_commit()
  
    
    except Exception as e:
        db_ex.rollback()
        error = f"Fehler bei insert_customer, input:{input}.\nEorror: {e}\n"
        raise Exception(error)
    
    finally:
        db_ex.close()
      
       
            
def update_customer_settings(table, customer_id, insert:dict):
    
    db_ex = DBExecutor()
    db_ex.open_connection_db() 
    
    columns = ""
    for k in insert.keys():
        columns=f"{columns}{k}=:{k}, "
    
    
    print(columns)
    print("insert bei update_customer_settings", insert)
    columns = columns[:-2]
    
    try:
        sql = f"""UPDATE {table}
                    SET {columns} 
                    WHERE customer_id={customer_id}"""

        db_ex.execute_and_commit(sql, insert)
        
    
    except Exception as e:
        error=f"Fehler bei update_customer_settings, table:{table}, customer_id{customer_id}"\
              f", insert:{insert}.\nError:{e}\n"
        raise Exception(error)
    
    finally:
        db_ex.close()




if __name__ == "__main__":

    dic = {
           'reference_account': 'z-bank'
          }
    table = "financials"
    test = update_customer_settings(table, 1, dic)