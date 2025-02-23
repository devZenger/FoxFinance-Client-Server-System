from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from service import RegistrationFormVertification

from repository import InsertCustomer

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
   password: str
    

@router.post("/create_costumer_account/")
async def create_account(accountform: AccountForm):
   
   data = accountform.model_dump()
   rfv = RegistrationFormVertification()
   
   errors = [] 
   
   for key, value in data.items():
      try :
         setattr(rfv, key, value)
         
      except Exception as e:
         errors.append(f"Fehlerhafte eingabe für {key}: {e}")
   
   if errors:
      raise HTTPException(status_code=422, detail=errors)
   
   try:
      dic = rfv.to_dict()
      fill_in = InsertCustomer()
      fill_in.insert(dic)
   except Exception as e:
      errors.append(f"Konnte Daten nicht speicher: {e}")
   
   if errors:
      raise HTTPException(status_code=500, detail=errors)
          
   return {"messeage": "gespeichert"}