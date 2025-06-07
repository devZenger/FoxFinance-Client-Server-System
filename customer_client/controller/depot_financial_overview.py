from model import FinancialHistory
from view import Display


class DepotFinancialOverview:
    def __init__(self):
        self.title = "Kontoübersicht"
        self.options = {"1. Die letzten drei Monate": "last_three",
                        "2. Die letzten zwölf Monate": "last_twelve",
                        "3. Zeitraum eingeben": "timespan",
                        "4. Konto anzeigen": "start",
                        "5. zurück": "back"}

        self.display_menu = Display()

    def run(self, token):
        self.fin_history = FinancialHistory()
        self.form_names = self.fin_history.form_names

        self.display_menu.display_title(self.title)

        choice = "start"

        while True:
            match choice:
                case "start":
                    request = self.fin_history.get_actual_balance(token)
                    self.show_info(request)
                    choice = "option"

                case "last_three":
                    request = self.fin_history.get_last_three_months(token)
                    self.show_table(request)
                    choice = "option"

                case "last_twelve":
                    request = self.fin_history.get_last_twelve_months(token)
                    self.show_table(request)
                    choice = "option"

                case "timespan":
                    form_filled = self.display_menu.display_form(self.form_names, self.fin_history)
                    if form_filled:
                        request = self.fin_history.get_fin_transaction_by_timespan(token)
                        self.show_table(request)
                    choice = "option"

                case "back":
                    return "start"

                case "option":
                    choice = self.display_menu.display_options(self.options)

                case _:
                    choice = "option"

    def show_info(self, input):

        if input is True:
            self.display_menu.display_info(self.fin_history.response)

        elif input is False:
            self.display_menu.display_info(self.fin_history.response)
        else:
            self.display_menu.display_info("unbekannter Fehler")

    def show_table(self, input):

        if input is True:
            self.display_menu.display_table(self.fin_history.response, self.fin_history.column_names)

        elif input is False:
            self.display_menu.display_info(self.fin_history.response)
        else:
            self.display_menu.display_info("keine Verbindung")
