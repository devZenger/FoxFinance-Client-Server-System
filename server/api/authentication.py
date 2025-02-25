from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LoginForm(BaseModel):
    email: str
    password: str
    

@router.post("/login/")
async def create_account(loginform: LoginForm):
    
    login_input = loginform.model_dump()
    
    
    
    return {"message": "Accoount created"}