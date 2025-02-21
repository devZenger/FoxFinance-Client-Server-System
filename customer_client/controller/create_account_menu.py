import requests

from view import DisplayMenuChoice
from view import  DisplayMenuForm

from model import RegistrationForm

from .menu_base import MenuBase
from .welcome_menu import WelcomeMenu

from .login_menu import LoginMenu




class CreateAccountMenu(MenuBase):         
    def __init__(self):
        self.menu_title = "Konto erstellen"
        self.form = RegistrationForm()
        self.form_names = {
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
        self.menu_points = {
            "1. Account erstellen": self.create_account,
            "2. abbrechen Zurück zum Hauptmenü:": self.back
        }
        
        super().__init__(DisplayMenuForm(self.menu_title, self.menu_points, self.form_names, self.form))

    def back(self):
        print("zurück")
        main_menu = WelcomeMenu()
        main_menu.show()
    
    def create_account(self):
        print("Bitte Eingaben2 überprüfen")
        url =  'http://127.0.0.1:5000/create_customer_account/'
        
        response = requests.post(url, json = self.to_fill.to_dict())
        if response.status_code == 200:
            print ("Empfangen:", response.json())
            print("Account erstellt")
        else:
            print("Fehler", response.status_code)