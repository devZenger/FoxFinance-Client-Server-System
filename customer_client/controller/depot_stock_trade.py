from view import Display
from model import StockActions


class DepotStockTrade:
    def __init__(self, token, options):

        self.stock_actions = StockActions(token)

        self.title = "Aktienhandel"
        self.title_stock = "Welche Aktie: "

        self.information = "Derzeit nur von DAX Unternehmen möglich"

        self.options = options
        self.options_make_trade = {"1. Handel abschließen": "make_trade",
                                   "2. Abrechen": "options"}

    def run(self):

        display_menu = Display()

        search_form_names = self.stock_actions.search_form_names
        trade_form_names = self.stock_actions.trade_form_names

        display_menu.display_title_and_infos(self.title, self.information)

        choice = "input_stock"

        while True:
            match choice:

                case "input_stock":
                    form_filled = display_menu.display_form(search_form_names, self.stock_actions)
                    if form_filled:
                        choice = self.stock_actions.stock_search()
                    else:
                        choice = "options"

                case "several_stocks":
                    stock_information = self.stock_actions.stock_list
                    display_menu.display_title_and_infos(self.title_stock, stock_information)
                    choice = "input_stock"

                case "single_stock":
                    form_filled = display_menu.display_form(trade_form_names, self.stock_actions)
                    if form_filled:
                        display_menu.display_dic(self.stock_actions.to_dict())
                        choice = display_menu.display_options(self.options_make_trade)
                    else:
                        choice = "options"

                case "no_stocks":
                    title_no_stocks = "Ergebnis"
                    no_stocks = "Die Aktie konnte nicht gefunden werden"
                    display_menu.execute(title_no_stocks, no_stocks)
                    choice = "options"

                case "make_trade":
                    response = self.stock_actions.stock_trade()
                    if response:
                        trade = "Handel erfolgreich."
                    else:
                        trade = "Handel konnte nicht abgechlossen werden."
                    display_menu.display_title_and_infos(self.title, trade)
                    choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options)
                    return choice

                case _:
                    display_menu.display_info("Programmfehler im Menü")
                    return "start"
