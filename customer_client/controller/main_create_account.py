import requests

from view import  DisplayMenu, display_response
from model import RegistrationForm

from model import Validation

#from .server_url import server_URL
#from .login_menu import LoginMenu


class CreateAccountMenu:         
    def __init__(self):
        self.title = "Konto erstellen"
        self.information = "Bitte Ausfüllen"
        self.options = {
            "1. Account erstellen": "create_account",
            "2. abbrechen Zurück zum Hauptmenü:": "discontinue"
        }
        self.options_failure = {
            "1. Wollen Sie wiederholen?":"start",
            "2. abbrechen Zurück zum Hauptmenü:": "discontinue"
        }
        
    def run(self):
        display_menu = DisplayMenu()
        self.regis_form = RegistrationForm()
        form_names = self.regis_form.form_names


        choice = "start"
        while True:
            match choice:
                case "start":
                    display_menu.display_title_and_infos(self.title, self.information)
                    display_menu.display_form(form_names, self.regis_form)
                    display_menu.display_filled_form()
                    choice = display_menu.display_options(self.options)
                
                case "create_account":
                    if self.regis_form.post_registration_form():
                        choice = "validation"
                    else:
                        choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options_failure)
                
                case "validation":
                    validate = ValidationControl()
                    
                    

                case "discontinue":
                    return "start"