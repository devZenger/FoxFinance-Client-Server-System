import requests

from view import DisplayMenuLogin
from model import LoginForm

from .server_url import server_URL
from .menu_base import MenuBase


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
        url =  f"{server_URL}/token"
        print(url)
        response = requests.post(url, json = self.login_form.to_dict())
        if response.status_code == 200:
            print ("Empfangen:", response.json())
            print("Account erstellt")
        else:
            print("Fehler", response.status_code)

    def discontinue(self):
        from .welcome_menu import WelcomeMenu
        start = WelcomeMenu()
        start.show()