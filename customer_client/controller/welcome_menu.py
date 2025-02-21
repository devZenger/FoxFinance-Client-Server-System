import requests

from view import DisplayMenuChoice
from view import  DisplayMenuForm

from model import RegistrationForm

from .menu_base import MenuBase

from.create_account_menu import CreateAccountMenu

from .login_menu import LoginMenu


class WelcomeMenu(MenuBase):
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
    