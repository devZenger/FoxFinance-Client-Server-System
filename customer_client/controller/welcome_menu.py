import requests

from view.display_menus import DisplayMenuChoice
from model.forms import RegistrationForm

class MenuBase:
   
    def __init__(self, title, menu_points, display_choice, infos = "", form = None):
        if form is None:
            form = {}
            
        self.menu_title = title
        self.menu_points = menu_points
        self.display_choice = display_choice
        self.infos = infos
        self.form = form
    
    
    def show(self):
        self.display_choice.execute_menu(self.menu_title, self.menu_points, self.infos, self.form)
        
        
 
 
class CreateAccount(MenuBase):
    menu_title = "Konto erstellen"
    form = RegistrationForm()
    
    menu_form = {
        "Familiennamen": form.last_name,
        "Vornamen": form.first_name,
        "Straße": form.street,
        "Hausnummer": form.house_number,
        "PLZ": form.zip_code,
        "Wohnort": form.city,
        "Geburtstag": form.birthday,
        "E-Mail Adresse":form.email,
        "Handynummer": form.phone_number,
        "Referenzkonto (IBAN)": form.reference_acccount,
        "Passwort": form.password   
    }
    
    def back(self):
        print("zurück")
        main_menu = MainMenu()
        main_menu.show()
    
    def create_account(self):
        print("Account erstellt")
        
    
    menu_points = {
        "Account erstellen": create_account,
        "Zurück zum Hauptmenü:": back
    }
  
      
    
    def __init__(self):
        super().__init__(self.menu_title, self.menu_points, DisplayMenuChoice(), self.menu_form)
        
        


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
        "1.Beispieldepot betrachten": example_portfolio,
        "2.Konto erstellen": create_account,
        "3.Login": login,
        "4.Informationen": information,
        "5.beenden": end_programm
        }

    def __init__(self):
        super().__init__(self.menu_title, self.menu_points, DisplayMenuChoice(), self.info)
    