from view import DisplayMenuInput2
from model import Information


class DepotInformation:
    def __init__(self, token):
        self.title = "Informationen"
        self.information = "Erstellt für tests"
        self.token = token

        self.options = {"1. Server anfragen: ": "stock_search"}

    def run(self):
        display_menu = DisplayMenuInput2(self.title)
        self.information = Information(self.token)
        form_names = self.information.form_names

        display_menu.execute()

        choice = "stock_search"

        while True:
            match choice:

                case "stock_search":
                    print("debug start menu")
                    choice = display_menu.execute_form(
                        form_names, self.information)

                case "form_filled":
                    self.send_search_request()
                    print("debug nächser schritt")
                    choice = "options"

                case "options":
                    print("debug options")
                    choice = display_menu.excute_options(self.options)

                case "stock_buy":
                    print("in bearbeitung")

    def send_search_request(self):

        self.information.get_information()
