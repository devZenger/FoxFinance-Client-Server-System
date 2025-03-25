from fastapi import APIRouter, HTTPException

from pydantic import BaseModel


from service import CustomerRegistration

router = APIRouter()

class AccountForm(BaseModel):
   last_name: str
   first_name: str
   street: str
   house_number: str
   zip_code: str
   city: str
   birthday: str
   email: str
   phone_number: str
   reference_account: str
   fin_amount: str
   password: str
    

@router.post("/create_costumer_account/")
async def create_account(accountform: AccountForm):   
   data = accountform.model_dump()
   customer_datas = CustomerRegistration()
   
   errors = [] 
   
   for key, value in data.items():
      try :
         setattr(customer_datas, key, value)
         
      except Exception as e:
         print(f"Fehlerhafte eingabe für {key}: {e}")
         errors.append(f"Fehlerhafte eingabe für {key}: {e}")
   
   if errors:
      raise HTTPException(status_code=422, detail=str(errors))
   
   
   try:
      customer_datas.insert_db()
      
   except Exception as e:
      raise HTTPException(status_code=422, detail=str(e))
   
   
  
   
          
