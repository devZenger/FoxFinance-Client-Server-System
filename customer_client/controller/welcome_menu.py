import requests

from view import DisplayMenuChoice
from view import  DisplayMenuForm

from model import RegistrationForm

from .menu_base import MenuBase

from .login_menu import LoginMenu


 
class CreateAccount(MenuBase):         
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
        main_menu = MainMenu()
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
        login = LoginMenu()
        login.show()

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
    