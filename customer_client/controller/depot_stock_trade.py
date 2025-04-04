from view import DisplayMenu
from model import StockActions


class DepotStockTrade:
    def __init__(self, token, options):
        self.title = "Aktienhandel"
        self.title2 = "Welche Aktie: "

        self.information = "Derzeit nur von DAX Unternehmen möglich"
        self.token = token

        self.options = options

        self.options_make_trade = {"1. Handel abschließen": "make_trade", "2. Abrechen": "options"}

    def run(self, isin=""):

        display_menu = DisplayMenu()
        stock_actions = StockActions(self.token)

        search_form_names = stock_actions.search_form_names
        trade_form_names = stock_actions.trade_form_names

        display_menu.display_title_and_infos(self.title, self.information)

        if isin == "":
            choice = "input_stock"
        else:
            choice = "single_stock"

        while True:
            match choice:

                case "input_stock":
                    choice = display_menu.display_form(
                        search_form_names, stock_actions)

                case "form_filled":
                    choice = stock_actions.stock_search()

                case "several_stocks":
                    stock_information = stock_actions.stock_list
                    display_menu.display_title_and_infos(
                        self.title2, stock_information)
                    choice = "input_stock"

                case "single_stock":
                    display_menu.display_form(trade_form_names, stock_actions)
                    
                    display_menu.display_dic(stock_actions.to_dict())

                    choice = display_menu.display_options(
                        self.options_make_trade)

                case "no_stocks":
                    title_no_stocks = "Ergebnis"
                    no_stocks = "Die Aktie konnte nicht gefunden werden"
                    display_menu.execute(title_no_stocks, no_stocks)
                    choice = "options"

                case "make_trade":
                    response = stock_actions.stock_trade()
                    display_menu.display_title_and_infos(self.title, response)
                    choice = "options"

                case "options":
                    print("debug options")
                    choice = display_menu.display_options(self.options)

                case _:
                    return choice
