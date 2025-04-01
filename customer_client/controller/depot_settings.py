from view import DisplayMenu
from model import SettingsForm


class Settings:
    def __init__(self, token, options):

        self.token = token
        self.options = options

        self.title ="Kontoeinstelungen ändern"

        self.information = "Was möchten Sie ändern?"
        self.information_2time = "Möchten Sie noch weiteres ändern ?"

        self.options_settings = {"1. Adresse":"adress",
                                 "2. Telefonnummer":"phone_number",
                                 "3. Email Adresse": "email_adress",
                                 "4. Referenzkonto": "reference_account",
                                 "5. Passwort" : "password",
                                 "6. abbrechen": "discountinue"}

        self.options_make_change = {"1. Änderungen vornehmen": "make_change",
                                    "2. abbrechen": "start"}

    def run(self):

        display_menu = DisplayMenu()
        self.settings = SettingsForm(self.token)

        current_settings = self.settings.current_settings()

        display_menu.display_info(current_settings)

        choice = "start"
        first = True

        while True:
            match choice:

                case "start":
                    display_menu.display_title(self.title)
                    if first is True:
                        display_menu.display_info(self.information)
                        first = False
                    else:
                        display_menu.display_info(self.information_2time)

                    choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options_settings)

                case "adress":
                    display_menu.display_form(self.settings.form_names_adress, self.settings)
                    display_menu.display_filled_form()
                    setting_type = "adress"
                    choice = "conform_change"

                case "phone_number":
                    display_menu.display_form(self.settings.form_names_phone_number, self.settings)
                    display_menu.display_filled_form()
                    setting_type = "phone_number"
                    choice = "conform_change"

                case "email_adress":
                    display_menu.display_form(self.settings.form_names_email_adress, self.settings)
                    display_menu.display_filled_form()
                    setting_type = "email"
                    choice = "conform_hange"

                case "reference_account":
                    display_menu.display_form(self.settings.form_names_reference_account, self.settings)
                    display_menu.display_filled_form()
                    setting_type = "reference_account"
                    choice = "conform_change"

                case "password":
                    display_menu.display_form(self.settings.form_names_password, self.settings)
                    display_menu.display_filled_form()
                    setting_type = "password"
                    choice = "conform_change"

                case "conform_change":
                   choice = display_menu.display_options(self.options_make_change)

                case "make_change":
                    response = self.settings.transmit_changes(setting_type)
                    print(response)
                    choice = "options"

                case "error":
                    display_menu.display_info(SettingsForm.error)
                    choice = "options"

                case "discountinue":
                    return "start"

                case _:
                    choice = "options"
