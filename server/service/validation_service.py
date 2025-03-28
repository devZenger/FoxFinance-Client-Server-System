import random
from pydantic import BaseModel

from repository import simple_search, insert_one_table, update_one_table

class Code(BaseModel):
    code:int

def create_validation(email):
    
    try: 
        result = simple_search("customers", "email", email)

        result = result["row_result0"]
        print("result")
        print(result)
    except:
        return "Email Addresse konnte nicht gefunden werden"
    
    
    check = find_customer_id(result["customer_id"])
    
    code = random.randint(100_000, 999_999)
    
    update = {"validation_number": code}
    condition = {"customer_id":result["customer_id"]}

    if check:
        update_one_table("validation", update, condition)
            
    else:
        condition.update(update)
        insert_one_table("validation", condition)
        
    return {"validation_number":code}



def find_customer_id(search):
    
    result = simple_search("validation", "customer_id", search)
    result = result["row_result0"]
    if bool(result):
        return True
    else:
        return False

def activate_account(code:Code):
    
    code_dic = code.model_dump()
    
    result = simple_search("validation", "validation_number", code_dic)
    result = result["row_result0"]
    
    
    
    


        

if __name__ == "__main__":
    

    email = "zoe"

    answer = create_validation(email)
    
    print("answer ist ", answer)
    
