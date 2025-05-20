from repository import update_customer_settings, simple_search
from schemas import Settings

from .customer_registration import CustomerRegistration
from utilitys import bank_account_decode

class SettingsService(CustomerRegistration):

    def __init__(self):

        super().__init__()

    def update_service(self, customer_id, new_settings: Settings):
        self.customer_id = customer_id
        self.insert_dic = {}
        self.table = ""

        match new_settings.transmission_type:

            case "adress":
                self.table = "customer_adresses"
                self.street = new_settings.street
                self.house_number = new_settings.house_number
                self.city = new_settings.city
                self.zip_code = new_settings.zip_code

                self.insert_dic = {
                    "street": self.street,
                    "house_number": self.house_number,
                    "zip_code": self.zip_code,
                    "city": self.city
                }

            case "phone_number":
                self.table = "customers"
                self.phone_number = new_settings.phone_number

                self.insert_dic = {
                    "phone_number": self.phone_number
                }

            case "email":
                self.table = "customers"
                self.email = new_settings.email

                self.insert_dic = {
                    "email": self.email
                }

            case "reference_account":
                self.table = "financials"
                self.reference_acccount = new_settings.reference_account

                self.insert_dic = {
                    "reference_account": self.reference_acccount
                }

            case "password":
                self.table = "authentication"
                self.password = new_settings.password

                self.insert_dic = {
                    "password": self.password
                }

        try:
            update_customer_settings(self.table, self.customer_id,
                                     self.insert_dic)

        except Exception as e:
            print("Fehler bei update:service (settings_service Z:83)")
            raise Exception(e)

    def search_current_settings(self, customer_id):
        current_settings = {}

        search_parameters = {"customer_adresses": "adress",
                             "customers": "customers",
                             "financials": "reference_account"}

        for key, value in search_parameters.items():
            response = simple_search(key, "customer_id", customer_id)
            print(response)
            current_settings[value] = response["row_result0"]

        current_settings["reference_account"]["reference_account"] = bank_account_decode(current_settings["reference_account"]["reference_account"])

        return current_settings


if __name__ == "__main__":

    customer_id = 1

    settings_service = SettingsService()

    answer = settings_service.search_current_settings(customer_id)

    print(" ")

    print(answer)

    print(" ")
