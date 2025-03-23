from pydantic import BaseModel

from .customer_registration import CustomerRegistration

class Settings(BaseModel):
    transmission_type: str
    street: str | None = None
    house_number: str | None = None
    city: str | None = None
    zip_code: str | None = None
    phone_number: str | None = None
    email: str | None = None
    reference_account: str | None = None
    password: str | None = None
    

class SettingsService(CustomerRegistration):
    
    def __init__(self):
    
        super().__init__()
    
    def run_service(self, new_settings:Settings):
        
        match new_settings.transmission_type:
            
            case "adress":
                self.street = new_settings.street
                self.house_number = new_settings.house_number
                self.city = new_settings.city
                self.zip_code = new_settings.zip_code
            
            case "phone_number":
                self.phone_number = new_settings.phone_number
            
            case "email":
                self.email = new_settings.email
                
            case "reference_account":
                self.reference_acccount = new_settings.reference_account
                
            case "password":
                self.password = new_settings.password
    
    def insert_db(self):
        pass             