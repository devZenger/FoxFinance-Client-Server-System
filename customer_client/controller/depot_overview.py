from model import DepotHistory
from view import DisplayMenu


class DepotOverview:
    def __init__(self, token):

        self.token = token
        self.depot = None

        self.title = "Depotübersicht"
        self.option = {"1. die letzten drei Monate": "last_three",
                       "2. die letzten zwölf Monate": "last twelve",
                       "3. Zeitraum einbegen": "timespan",
                       "4. Depot anzeigen": "start",
                       "5. zurück": "back"}

    def run(self):
        self.display_menu = DisplayMenu()
        self.depot = DepotHistory(self.token)
        self.form_names = self.depot.form_names

        self.display_menu.display_title(self.title)

        choice = "start"

        while True:
            match choice:
                case "start":
                    request = self.depot.get_all_stocks()
                    self.show_table(request)
                    choice = "option"

                case "last_three":
                    request = self.depot.get_last_three_months()
                    self.show_table_timespan(request)
                    choice = "option"

                case "last_twelve":
                    request = self.depot.get_last_twelve_months()
                    self.show_table_timespan(request)
                    choice = "option"

                case "timespan":
                    self.display_menu.display_form(self.form_names)
                    request = self.depot.get_transaction_by_timespan()
                    self.show_table_timespan(request)
                    choice = "option"

                case "back":
                    return "start"

                case "option":
                    choice = self.display_menu.display_options(self.option)

                case _:
                    choice = "option"

    def show_table(self, input):

        if input is True:
            self.display_menu.display_table(
                self.depot.response, self.depot.column_names)

        else:
            self.display_menu.display_info(self.depot.response)

    def show_table_timespan(self, input):

        if input is True:
            self.display_menu.display_table(
                self.depot.response, self.depot.column_names_timespan)

        else:
            self.display_menu.display_info(self.depot.response)
