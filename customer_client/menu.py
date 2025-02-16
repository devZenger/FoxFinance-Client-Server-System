import requests

from menubase import MenuBase


     
class CreateAccount(MenuBase):
    menu_title = "Konto erstellen"
    menu_formular = {"Name": " ", "E-mail Adresse": " ", "Handynummer": " ", "Passwort": " "}
    
    def run(self):
        filled_formular = self.execute_formular()
        
        print("Create Account")
        for k, v, in filled_formular.items():
            print(f"{k} = {v}")
 
 
class Login(MenuBase):
    menu_title = "Login Menü"
    menu_formular = {"E-mail Adresse: ": " ", "Passwort :": " "}

    def login_check(self):
        filled_formular = self.execute_formular()

        print("formular test")
        for k, v, in filled_formular.items():
            print(f"{k} = {v}")

    def __init__(self):
        super().__init__(self.menu_title, self.menu_formular)
        

class Information(MenuBase):
    menu_title = "Informationen"
    response = requests.get('http://127.0.0.1:5000/information')
    infos = response #"Fox Finance bietet umfassenden Service rund um das Thema Aktien\n"        
    
    def back(self):
        print("zurück")
        main_menu = MainMenu()
        main_menu.run()
    
    menu_points = {infos: " ", "1. zurück": back}
    
    def __init__(self):
        super().__init__(self.menu_title, self.menu_points)
        
    def run(self):
        self.execute_choice()

class MainMenu(MenuBase):
    menu_title = "Hauptmenü"
    
    def example_portfolio(self):
        print("Beispieldepot in Bearbeitung")

    def create_account(self):
        print("Konto erstellen")

    def login(self):
        login = Login()
        login.login_check()

    def information(self):
        information = Information()
        information.run()

    def end_programm(self):
        print("Programm beenden")
        exit(0)

    menu_points = {
        "1.Beispieldepot betrachten": example_portfolio,
        "2.Konto erstellen": create_account,
        "3.Login": login,
        "4.Informationen": information,
        "5.beenden": end_programm
        }

    def __init__(self):
        super().__init__(self.menu_title, self.menu_points)
  
    def run(self):
        self.execute_choice()
    
        