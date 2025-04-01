from view import DisplayMenu
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
        login_form = LoginForm()
        form_names = login_form.form_names

        display_menu.display_title(self.title)

        choice = "start"
        while True:
            match choice:
                case "start":
                    display_menu.display_info("Bitte Anmeldedaten eingeben")
                    display_menu.display_form(form_names, login_form)
                    choice = display_menu.display_options(self.options)

                case "login":

                    login_success = login_form.post_login_form()

                    if login_success:
                        return True, login_form.response
                    else:
                        display_menu.display_info(login_form.response)
                        choice = display_menu.display_options(self.options2)

                case "abbrechen":
                    return False, None
