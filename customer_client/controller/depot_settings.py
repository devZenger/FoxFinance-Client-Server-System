from view import Display
from model import SettingsForm


class Settings:
    def __init__(self, options):
        self.title = "Kontoeinstelungen ändern"
        self.information = "Was möchten Sie ändern?"
        self.information_2time = "Möchten Sie noch weiteres ändern ?"

        self.options = options
        self.options_settings = {"1. Adresse": "adress",
                                 "2. Telefonnummer": "phone_number",
                                 "3. Email Adresse": "email_adress",
                                 "4. Referenzkonto": "reference_account",
                                 "5. Passwort": "password",
                                 "6. abbrechen": "discountinue"}

        self.options_make_change = {"1. Änderungen vornehmen": "make_change",
                                    "2. abbrechen": "start"}

    def run(self, token):
        settings = SettingsForm()
        display_menu = Display()
        choice = "start"
        first = True

        while True:
            match choice:

                case "start":
                    display_menu.display_title(self.title)

                    status = settings.current_settings(token)
                    if status:
                        display_menu.display_dic_in_dic(settings.data)

                        if first is True:
                            display_menu.display_info(self.information)
                            first = False
                        else:
                            display_menu.display_info(self.information_2time)
                    else:
                        display_menu.display_info(settings.response)

                    choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options_settings)

                case "adress":
                    form_filled = display_menu.display_form(settings.form_names_adress, settings)
                    if form_filled:
                        display_menu.display_filled_form()
                        setting_type = "adress"
                        choice = "conform_change"
                    else:
                        choice = "options"

                case "phone_number":
                    form_filled = display_menu.display_form(settings.form_names_phone_number, settings)
                    if form_filled:
                        display_menu.display_filled_form()
                        setting_type = "phone_number"
                        choice = "conform_change"
                    else:
                        choice = "options"

                case "email_adress":
                    form_filled = display_menu.display_form(settings.form_names_email_adress, settings)
                    if form_filled:
                        display_menu.display_filled_form()
                        setting_type = "email"
                        choice = "conform_hange"
                    else:
                        choice = "options"

                case "reference_account":
                    form_filled = display_menu.display_form(settings.form_names_ref_account, settings)
                    if form_filled:
                        display_menu.display_filled_form()
                        setting_type = "reference_account"
                        choice = "conform_change"
                    else:
                        choice = "options"

                case "password":
                    form_filled = display_menu.display_form(settings.form_names_password, settings)
                    if form_filled:
                        display_menu.display_filled_form()
                        setting_type = "password"
                        choice = "conform_change"
                    else:
                        choice = "options"

                case "conform_change":
                    choice = display_menu.display_options(self.options_make_change)

                case "make_change":
                    response = settings.transmit_changes(setting_type, token)
                    choice = response

                case "error":
                    display_menu.display_title(self.title)
                    display_menu.display_info(settings.response)
                    choice = "options"

                case "discountinue":
                    return "start"

                case _:
                    choice = "options"
