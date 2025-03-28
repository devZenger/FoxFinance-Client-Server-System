from passlib.context import CryptContext
from pydantic import BaseModel

from repository import insert_customer

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


class CustomerRegistration:
    def __init__(self, account_form:AccountForm):
        self._last_name = None
        self._first_name = None
        self._street = None
        self._house_number = None
        self._zip_code = None
        self._city = None
        self._birthday = None
        self._email = None
        self._phone_number = None
        self._reference_account = None
        self._fin_amount = None
        self._password = None
        
        errors = []
        
        for key, value in account_form.model_dump().items():
            try:
                setattr(self, key, value)
         
            except Exception as e:
                print(f"Fehlerhafte eingabe für {key}: {e}")
                errors.append(f"Fehlerhafte eingabe für {key}: {e}")
        
        
        if errors:
            raise Exception(errors)
        
        
    
    # last name
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, input):
        if len(input) >= 2:
            self._last_name = input
        else:
            raise ValueError("Mindestens zwei Zeichen")
    
    # first name
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, input):
        if len(input) >= 2:
            self._first_name = input  
        else:
             raise ValueError("Mindestens zwei Zeichen")
    
    #  street
    @property
    def street(self):
        return self._street
    
    @street.setter
    def street(self, input):
        if len(input) >= 2:
            self._street = input
        else:
            raise ValueError("Mindestens zwei Zeichen")
        
    # house number
    @property
    def house_number(self):
        return self._house_number
    
    @house_number.setter
    def house_number(self, input):
        if len(input) >= 1:
            self._house_number = input
        else:
            raise ValueError("Mindestens zwei Zeichen")
    
    # city
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, input):
        if len(input) >= 2:
            self._city = input
        else:
            raise ValueError("Mindestens zwei Zeichen")
    
    # zip code
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, input):
        if len(input) >= 2:
            self._zip_code = input
        else:
            raise ValueError("Mindestens zwei Zeichen")
    
    # birthday
    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, input):
        if len(input) >= 2:
            self._birthday = input
        else:
            raise ValueError("Mindestens zwei Zeichen")
    
    # email
    @property
    def email(self):
        return self._birthday
    
    @email.setter
    def email(self, input):
        if len(input) >= 2:
            self._email = input
        else:
            raise ValueError("Mindestens zwei Zeichen")
    
    # phone number
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, input):
        if len(input) >= 2:
            self._phone_number = input
        else:
            raise ValueError("Mindestens zwei Zeichen")
    
    # reference account
    @property
    def reference_account(self):
        return self._reference_account
    
    @reference_account.setter
    def reference_account(self, input):
        if len(input) >= 2:
            self._reference_account = input
        else:
            raise ValueError("Mindestens zwei Zeichen")
    
    # balance
    @property
    def fin_amount(self):
        return self._fin_amount
    
    @fin_amount.setter
    def fin_amount(self, input):
        if len(input) >= 1:
            self._fin_amount = input
        else:
            self._fin_amount = 0
    
    # passwort
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, input):
        if len(input) >= 2:
            password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            self._password = password_context.hash(input)
        else:
            raise ValueError("Mindestens zwei Zeichen")
        

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "street": self.street,
            "house_number": self.house_number,
            "zip_code": self.zip_code,
            "city": self.city,
            "birthday": self.birthday,
            "email": self.email,
            "phone_number": self.phone_number,
            "reference_account": self.reference_account,
            "fin_amount": self.fin_amount,
            "password": self.password
        }
    
    def insert_db(self):
        
        
        as_dic = self.to_dict()
        
        try:
            insert_customer(as_dic)
   
        
        except Exception as e:
            print(e)
            raise ValueError(e)        
                
        
        


