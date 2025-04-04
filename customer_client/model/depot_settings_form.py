from .registration_form import RegistrationForm
from .server_request import ServerRequest


class SettingsForm(RegistrationForm):
    def __init__(self, token):
        self.token = token
        
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

    def transmit_changes(self, type: str):

        to_transmit = {}

        match type:

            case "adress":
                to_transmit = {"transmission_type": "adress",
                               "street": self.street,
                               "house_number": self.house_number,
                               "city": self.city,
                               "zip_code": self.zip_code}

            case "phone_number":
                to_transmit = {"transmission_type": "phone_number",
                               "phone_number": self.phone_number}
            case "email":
                to_transmit = {"transmission_type": "email",
                               "email": self.email}
            case "reference_account":
                to_transmit = {"transmission_type": "reference_account",
                               "reference_account": self.reference_account}
            case "password":
                to_transmit = {"transmission_type": "password",
                               "password": self.password}
            case _:
                return print("fehler")

        server_request = ServerRequest(self.token)

        url_part = "changesettings/"

        print(f"to transmit is {to_transmit}")

        status, self.response = server_request.make_post_request(
            url_part, to_transmit)

        del server_request

        if status:
            return "start"
        else:
            return "error"

    def current_settings(self):

        server_request = ServerRequest(self.token)

        url_part = "settings/"

        status, response = server_request.get_without_parameters(url_part)

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

        del server_request

        return status
