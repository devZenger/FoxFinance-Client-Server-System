from model import DepotHistory
from view import Display


class DepotOverview:
    def __init__(self):
        self.title = "Depotübersicht"
        self.options = {"1. Aktienhandel der letzten dreißig Tage": "last_30days",
                        "2. Aktienhandel der letzten drei Monate": "last_three",
                        "3. Zeitraum eingeben": "timespan",
                        "4. Depot anzeigen": "start",
                        "5. zurück": "back"}
        self.display_menu = Display()

    def run(self, token):
        self.depot = DepotHistory()
        self.form_names = self.depot.form_names
        self.display_menu.display_title(self.title)

        choice = "start"

        while True:
            match choice:
                case "start":
                    request = self.depot.get_all_stocks(token)
                    self.show_table(request)
                    choice = "option"

                case "last_30days":
                    request = self.depot.get_last_thirty_days(token)
                    self.show_table_timespan(request, "Die letzten dreißig Tage:")
                    choice = "option"

                case "last_three":
                    request = self.depot.get_last_three_months(token)
                    self.show_table_timespan(request, "Die letzten drei Monate:")
                    choice = "option"

                case "timespan":
                    form_filled = self.display_menu.display_form(self.form_names, self.depot)
                    if form_filled:
                        request = self.depot.get_transaction_by_timespan(token)
                        self.show_table_timespan(request)
                    choice = "option"

                case "back":
                    return

                case "option":
                    choice = self.display_menu.display_options(self.options)

                case _:
                    choice = "option"

    def show_table(self, input):

        if input is True:
            self.display_menu.display_table(self.depot.response, self.depot.column_names)

        else:
            self.display_menu.display_info(self.depot.response)

    def show_table_timespan(self, input, title=None):

        if input is True:
            if title is None:
                title = f"Vom {self.depot.start_time} bis {self.depot.end_time}:"
            self.display_menu.display_title(title)
            self.display_menu.display_table(self.depot.response, self.depot.column_names_timespan)

        else:
            self.display_menu.display_info(self.depot.response)
