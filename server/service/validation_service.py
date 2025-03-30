import random
from pydantic import BaseModel
from datetime import datetime, timezone, timedelta

from repository import simple_search, insert_one_table, update_one_table

class Code(BaseModel):
    validation_number:int = 0



def find_customer_id(search):
    
    result = simple_search("validation", "customer_id", search)
    print("result", result)
    #result = result["row_result0"]
    print("result ohne 0", result)
    if bool(result):
        return True
    else:
        return False



def create_validation(email):

    try: 
        result = simple_search("customers", "email", email)

        result = result["row_result0"]
        print("result")
        print(result)
    except:
        error = "Email Addresse konnte nicht gefunden werden"
        print(error)
        raise Exception(error)

    print("test")
    
    print(result["customer_id"])

    check = find_customer_id(result["customer_id"])
    
    print("check", check)

    code = random.randint(100_000, 999_999)

    update = {"validation_number": code}
    condition = {"customer_id":result["customer_id"]}

    if check:
        print("update:", update)
        print("condition", condition)
        update_one_table("validation", update, condition)

    else:
        condition.update(update)
        print("condition", condition)
        insert_one_table("validation", condition)

    
    return {"validation_number":code}



def activate_account(code:Code):
    
    code_dic = code.model_dump()
    
    print("code_dic", code_dic)
    
    result = simple_search("validation", "validation_number", code_dic["validation_number"])
    
    try:
        result = result["row_result0"]

        if result["validation_number"] == code_dic["validation_number"]:
            
            current_time = datetime.now(timezone.utc)
            validation_time_code = datetime.strptime(result["date"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            
            five_min = timedelta(minutes=5)
            
            time_dif = current_time-validation_time_code
            
            if time_dif <= five_min:
                condition_dic={"customer_id":result["customer_id"]}
                print("condition", condition_dic)
                update={"disabled":False}
                print("update", update)
                update_one_table("customers", update, condition_dic)
                return "Ihr Konto wurde aktiviert"
            else:
                return "Aktivierungscode abgelaufen"
        
    except:
        error="Der Aktivierungscode ist Fehlerhaft"
        raise Exception(error)
        
        
    
    
    
    


        

if __name__ == "__main__":
    
    code = Code()
    
    code.validation_number = 772220

    email = "toe"

    answer = activate_account(code)
    
    print("answer", answer)
    

    
