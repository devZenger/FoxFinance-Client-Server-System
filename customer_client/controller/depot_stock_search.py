from view import DisplayMenu
from model import StockActions


class DepotStockSearch:
    def __init__(self, token, options):
        self.title = "Aktiensuche"
        self.title2 = "Ergebnisse: "
        self.title3 = "Ergebnis: "
        self.information = "Derzeit nur Dax unternehmen möglich"
        self.token = token

        self.stock_information = None

        self.options = options

    def run(self):
        display_menu = DisplayMenu()
        stock_actions = StockActions(self.token)

        display_menu.display_title(self.title)

        choice = "stock_search"

        while True:
            match choice:

                case "stock_search":
                    display_menu.display_info(self.information)
                    choice = display_menu.display_form(
                        stock_actions.search_form_names, stock_actions)

                case "form_filled":
                    choice = stock_actions.stock_search()

                case "several_stocks":
                    stock_information = stock_actions.stock_list
                    display_menu.display_title_and_infos(
                        self.title2, stock_information)
                    choice = "options"

                case "single_stock":
                    display_menu.display_title(self.title3)
                    display_menu.display_dic_in_dic(
                        stock_actions.stock_information)
                    choice = "options"

                case "no_stocks":
                    display_menu.display_info(self.stock_information)
                    choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options)

                case "stock_buy":
                    isin = stock_actions.isin
                    return "buy_stocks", isin

                case _:
                    return choice, ""
