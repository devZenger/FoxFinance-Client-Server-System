from view import Display
from model import RegistrationForm, Validation


class CreateAccountMenu:
    def __init__(self):
        self.title = "Konto erstellen"
        self.information = "Bitte Ausfüllen"
        self.options = {
            "1. Konto erstellen": "create_account",
            "2. Abbrechen – Zurück zum Hauptmenü": "discontinue"
        }
        self.options_failure = {
            "1. Wollen Sie wiederholen?": "start",
            "2. Abbrechen – Zurück zum Hauptmenü": "discontinue"
        }

    def run(self):
        display_menu = Display()
        regis_form = RegistrationForm()
        form_names = regis_form.form_names
        validation = Validation()

        choice = "start"
        while True:
            match choice:
                case "start":
                    display_menu.display_title_and_infos(self.title, self.information)
                    form_filled = display_menu.display_form(form_names,
                                                            regis_form)
                    if form_filled:
                        display_menu.display_filled_form()
                        choice = display_menu.display_options(self.options)
                    else:
                        return "start"

                case "create_account":
                    if regis_form.post_registration_form():
                        choice = "validation"
                    else:
                        choice = "options"

                case "options":
                    display_menu.display_info("Konto konnte nicht erstellt werden")
                    choice = display_menu.display_options(self.options_failure)

                case "validation":
                    success, code = validation.get_activate_code(regis_form.email)

                    if success:
                        display_menu.display_dict(code)
                    else:
                        display_menu.display_info(code)

                    display_menu.display_form(validation.form_name, validation)

                    success = validation.send_activate_code()

                    display_menu.display_info(validation.response)

                    if success:
                        return "start"

                    else:
                        choice = "options"

                case "discontinue":
                    return "start"
