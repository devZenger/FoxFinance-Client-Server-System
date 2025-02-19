import requests

from view import DisplayMenuLogin

from .menu_base import MenuBase
from .welcome_menu import MainMenu

from model import LoginForm

class LoginMenu(MenuBase):
     
    def __init__(self):
        self.menu_title= "Login Menü:"
        self.login_form = LoginForm()
        self.login_names = {
            "email": "E-Mail Adresse",
            "password": "Passwort"
        }
        self.menu_points = {
        "1. Einloggen": self.login,
        "2. zurück": self.discontinue
        }
        
        super().__init__(DisplayMenuLogin(self.menu_title, self.menu_points, self.login_names, self.login_form))
        
    def login(self):
        url =  'http://127.0.0.1:5000/login_user/'
        
        response = requests.post(url, json = self.to_fill.to_dict())
        if response.status_code == 200:
            print ("Empfangen:", response.json())
            print("Account erstellt")
        else:
            print("Fehler", response.status_code)

    def discontinue(self):
        main_menu = MainMenu()
        main_menu.show()
