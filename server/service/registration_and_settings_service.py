from repository import insert_customer, simple_search, update_one_table
from utilities import bank_account_decode


def make_registration(new_account: dict, client_ip: str):
    new_account["client_ip"] = client_ip
    insert_customer(new_account)


def update_settings(customer_id, new_settings: dict):

    to_insert_customer = {}
    to_insert_address = {}
    to_insert_fin = {}
    to_insert_auth = {}

    customer_tab = False
    finanicals_tab = False
    address_tab = False
    authentication_tab = False

    for key, value in new_settings.items():
        if key in new_settings:

            if key == "street":
                to_insert_address[key] = value
                address_tab = True

            if key == "house_number":
                to_insert_address[key] = value
                address_tab = True

            if key == "city":
                to_insert_address[key] = value
                address_tab = True

            if key == "zip_code":
                to_insert_address[key] = value
                address_tab = True

            if key == "email":
                to_insert_customer[key] = value
                customer_tab = True
            if key == "phone_number":
                to_insert_customer[key] = value
                customer_tab = True

            if key == "reference_account":
                to_insert_fin[key] = value
                authentication_tab = True

            if key == "password":
                to_insert_auth[key] = value
                customer_tab = True

    update_condition = {"customer_id": customer_id}
    if customer_tab:
        update_one_table("customers", to_insert_customer, update_condition)
    if address_tab:
        update_one_table("customer_addresses", to_insert_address, update_condition)
    if authentication_tab:
        update_one_table("authentication", to_insert_auth, update_condition)
    if finanicals_tab:
        update_one_table("financials", to_insert_fin, update_condition)


def search_current_settings(customer_id):
    current_settings = {}

    search_parameters = {"customer_addresses": "adress",
                         "customers": "customers",
                         "financials": "reference_account"}

    for key, value in search_parameters.items():
        response = simple_search(key, "customer_id", customer_id)
        print(response)
        current_settings[value] = response["row_result0"]

    current_settings["reference_account"]["reference_account"] = bank_account_decode(
        current_settings["reference_account"]["reference_account"])

    return current_settings


if __name__ == "__main__":

    customer_id = 1

    answer = search_current_settings(customer_id)

    print(" ")

    print(answer)

    print(" ")
