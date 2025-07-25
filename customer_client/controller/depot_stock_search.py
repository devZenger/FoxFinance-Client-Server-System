from view import Display
from model import StockActions


class DepotStockSearch:
    def __init__(self, options):
        self.title = "Aktiensuche"
        self.title_findings = "Ergebnisse: "
        self.title_result = "Ergebnis: "
        self.information = "Derzeit nur Dax unternehmen möglich"
        self.options = options

    def run(self, token):
        display_menu = Display()
        stock_actions = StockActions()

        display_menu.display_title(self.title)

        choice = "stock_search"

        while True:
            match choice:

                case "stock_search":
                    display_menu.display_info(self.information)
                    form_filled = display_menu.display_form(stock_actions.search_form_names, stock_actions)
                    if form_filled:
                        choice = stock_actions.stock_search(token)
                    else:
                        choice = "options"

                case "several_stocks":
                    stock_information = stock_actions.stock_list
                    display_menu.display_title_and_infos(self.title_findings, stock_information)
                    choice = "options"

                case "single_stock":
                    display_menu.display_title(self.title_result)
                    display_menu.display_dic_in_dic(stock_actions.stock_information)
                    choice = "options"

                case "no_stocks":
                    display_menu.display_info(stock_actions.stock_information)
                    choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options)

                case _:
                    return choice
