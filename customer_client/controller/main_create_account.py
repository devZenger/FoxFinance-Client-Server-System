import requests

from view import  DisplayMenuForm, display_response
from model import RegistrationForm


from model import url_server
#from .server_url import server_URL

#from .login_menu import LoginMenu


class CreateAccountMenu:         
    def __init__(self):
        self.title = "Konto erstellen"
        
        self.options = {
            "1. Account erstellen": "account erstellen",
            "2. abbrechen Zurück zum Hauptmenü:": "abbrechen"
        }
        
    
    def run(self):
        display_menu = DisplayMenuForm(self.title)
        self.regis_form = RegistrationForm()
        form_names = self.regis_form.form_names


        choice = "start"
        while True:
            match choice:
                case "start":
                    print("start menu")
                    choice = display_menu.execute(self.options, form_names, self.regis_form)
                
                case "account erstellen":
                    #data = self.regis_form.to_dict()
                            
                    #for d,v in data.items():
                     #   print(f"{d} value = {v}")
                    
                    self.create_account()
                    
                    choice = "abbrechen"
                    
                case "abbrechen":
                    return "start"

        

    def create_account(self):
       
        
        url =  f"{url_server}/create_costumer_account/"
       
        #url =  'http://127.0.0.1:8000/create_costumer_account/'
      
        response = requests.post(url, json = self.regis_form.to_dict())

        if response.status_code == 200:
            output = f"\tEmpfangen:, {response.json()}\n  Account erstellt"
        else:
            output = f"\tFehler {response.status_code}"
        
        display_response(output)