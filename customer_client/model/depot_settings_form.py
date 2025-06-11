from .registration_form import RegistrationForm


class SettingsForm(RegistrationForm):
    def __init__(self):
        self.data = None

        self.form_names_adress = {
            "street": "Straße (ohne Hausnummer)",
            "house_number": "Hausnummer",
            "city": "Stadt",
            "zip_code": "Postleitzahl",
        }

        self.form_names_phone_number = {
            "phone_number": "Telefonnummer"
        }

        self.form_names_email_adress = {
            "email": "E-Mail Adresse",
        }

        self.form_names_ref_account = {
            "reference_account": "Referenzkonto",
        }

        self.form_names_password = {
            "password": "Passwort"
        }

        super().__init__()

        self.name_settings = self.form_names
        del self.name_settings["fin_amount"]

    def transmit_changes(self, type: str, token):

        to_transmit = {}

        match type:

            case "adress":
                to_transmit = {"street": self.street,
                               "house_number": self.house_number,
                               "city": self.city,
                               "zip_code": self.zip_code}

            case "phone_number":
                to_transmit = {"phone_number": self.phone_number}
            case "email":
                to_transmit = {"email": self.email}
            case "reference_account":
                to_transmit = {"reference_account": self.reference_account}
            case "password":
                to_transmit = {"password": self.password}
            case _:
                self.response = "Fehler, type konnte nicht zugeordnet werden"
                return "error"

        url_part = "changesettings/"

        status, self.response = self.server_request.make_patch_request(url_part, token, to_transmit)

        if status:
            return "start"
        else:
            return "error"

    def current_settings(self, token):

        url_part = "settings/"

        status, response = self.server_request.get_without_parameters(url_part, token)

        data_adress = {"Straße": f"{response["adress"]["street"]}",
                       "Hausnummer": f"{response["adress"]["house_number"]}",
                       "PLZ": f"{response["adress"]["zip_code"]}",
                       "Stadt": f"{response["adress"]["city"]}"}

        self.data = {"Adresse": data_adress}

        data_contact = {"Telefonnummer": f"{response["customers"]["phone_number"]}",
                        "Email": f"{response["customers"]["email"]}"}

        self.data["Kontaktdaten"] = data_contact

        data_bank = {"Referenzkonto": f"{response["reference_account"]["reference_account"]}"}

        self.data["Bankverbindung"] = data_bank

        return status
