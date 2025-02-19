import requests

from view import DisplayMenuChoice
from view import  DisplayMenuForm

from model import RegistrationForm

class MenuBase:
   
    def __init__(self, display_choice):
        self.display_choice = display_choice
    
    def show(self):
        self.display_choice.execute()
        
        
 
 
class CreateAccount(MenuBase):
    
        
    
    def back(self):
        print("zurück")
        main_menu = MainMenu()
        main_menu.show()
    
    def create_account(self):
        print("Account erstellt")
        
    
    menu_points = {
        "1. Account erstellen": create_account,
        "2. abbrechen Zurück zum Hauptmenü:": back
    }
  
      
    
    def __init__(self):
        self.menu_title = "Konto erstellen"
        self.form = RegistrationForm()
        
        self.menu_form_name = {
            "last_name": "Familiennamen",
            "first_name": "Vornamen",
            "street": "Straße",
            "house_number": "Hausnummer",
            "zip_code": "PLZ",
            "city": "Stadt",
            "birthday": "Geburtstag",
            "email" : "E-Mail Adresse",
            "phone_number": "Handynummer",
            "reference_account": "Referenzkonto (IBAN)",
            "password": "Passwort"
        }
        super().__init__(DisplayMenuForm(self.menu_title, self.menu_points, self.menu_form_name, self.form))
        

class MainMenu(MenuBase):
    menu_title = "Hauptmenü"
    info = "Hello World"
    
    def example_portfolio(self):
        print("Beispieldepot in Bearbeitung")

    def create_account(self):
        create_acc = CreateAccount()
        create_acc.show()
        

    def login(self):
        print ("Login")

    def information(self):
        print("info")

    def end_programm(self):
        print("Programm beenden")
        exit(0)

    menu_points = {
        "1. Beispieldepot betrachten": example_portfolio,
        "2. Konto erstellen": create_account,
        "3. Login": login,
        "4. Informationen": information,
        "5. beenden": end_programm
        }

    def __init__(self):
        super().__init__(DisplayMenuChoice(self.menu_title, self.menu_points, self.info))
    