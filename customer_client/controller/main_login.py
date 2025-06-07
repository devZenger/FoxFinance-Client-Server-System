from view import Display
from model import LoginForm


class LoginMenu:
    def __init__(self):
        self.title = "Konto anmelden"

        self.options = {
            "1. Anmelden": "login",
            "2. abbrechen, Zurück zum Hauptmenü:": "back"
        }
        self.options_failure = {
            "1. Erneut versuchen": "start",
            "2. abbrechen, Zurück zum Hauptmenü:": "back"
        }

    def run(self):
        display_menu = Display()
        login_form = LoginForm()
        form_names = login_form.form_names

        display_menu.display_title(self.title)

        choice = "start"
        while True:
            match choice:
                case "start":
                    display_menu.display_info("Bitte Anmeldedaten eingeben")
                    form_filled = display_menu.display_form(form_names, login_form)
                    if form_filled:
                        choice = display_menu.display_options(self.options)
                    else:
                        choice = "back"

                case "login":

                    login_success = login_form.post_login_form()

                    if login_success:
                        return True, login_form.response
                    else:
                        display_menu.display_info(login_form.response)
                        choice = display_menu.display_options(self.options_failure)

                case "back":
                    return False, None

    def start_example_account(self):
        email = "max@mustermann.de"
        pwd = "12345+-QWert"

        login_form = LoginForm()

        login_form.email = email
        login_form.password = pwd

        login_success = login_form.post_login_form()

        if login_success:
            return True, login_form.response
        else:
            return False, "Tut uns leidet, das Beispieldepot steht derzeit nicht zur Verfügung"
