import requests


from view import  DisplayMenu
from model import LoginForm



class LoginMenu:         
    def __init__(self):
        self.title = "Konto anmelden"
       
        self.options = {
            "1. Anmelden": "login",
            "2. abbrechen, Zurück zum Hauptmenü:": "abbrechen"
        }
        self.options2 = {
            "1. Erneut versuchen": "start",
            "2. abbrechen, Zurück zum Hauptmenü:": "abbrechen"
        }
        
    
    def run(self):
        display_menu = DisplayMenu()
        self.login_form = LoginForm()
        form_names = self.login_form.form_names

        display_menu.display_title(self.title)
     
        choice = "start"
        while True:
            match choice:
                case "start":
                    display_menu.display_info("Bitte Anmeldedaten eingeben")
                    display_menu.display_form(form_names, self.login_form)
                    choice = display_menu.display_options(self.options)
                
                case "login":
                    #data = self.login_form.to_dict()
                    login_success = self.login_form.post_login_form()
                    
                    if login_success:
                        return True, self.login_form.response
                    else:
                        display_menu.display_info(self.login_form.response)
                        choice = display_menu.display_options(self.options2)


                case "abbrechen":
                    return False, None

        
   
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