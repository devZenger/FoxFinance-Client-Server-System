import requests


from view import  DisplayMenuInput
from model import LoginForm



class LoginMenu:         
    def __init__(self):
        self.title = "Konto anmelden"
       
        self.options = {
            "1. Anmelden": "login",
            "2. abbrechen, Zurück zum Hauptmenü:": "abbrechen"
        }
        
    
    def run(self):
        display_menu = DisplayMenuInput(self.title)
        self.login_form = LoginForm()
        form_names = self.login_form.form_names

     
        choice = "start"
        while True:
            match choice:
                case "start":
                    choice = display_menu.execute(self.options, form_names, self.login_form)
                
                case "login":
                    #data = self.login_form.to_dict()
                             
                    token = self.send_request()
                    return token
                    
                    
                case "abbrechen":
                    return "start"

        
   
    def send_request(self):
        print("\tzum Test")
        
        #login_data = self.login_form.to_dict()
        #print(data)                     
       
       
        url =  'http://127.0.0.1:8000/token'
        
        response = requests.post(url, json = self.login_form.to_dict())
        
        if response.status_code == 200:
            print ("Empfangen:", response.json())
            print("eingeloggt")
            token = response.json()
            token["email"]= self.login_form.email
            return token 
        else:
            print("Fehler", response.status_code)