from view import Display
from model import StockActions


class DepotStockTrade:
    def __init__(self, options):
        self.title = "Aktienhandel"
        self.title_stock = "Welche Aktie: "

        self.information = "Derzeit nur von DAX Unternehmen möglich"

        self.options = options
        self.options_make_trade = {"1. Handel abschließen": "make_trade",
                                   "2. Abrechen": "options"}

    def run(self, token):
        stock_actions = StockActions()
        display_menu = Display()

        search_form_names = stock_actions.search_form_names
        trade_form_names = stock_actions.trade_form_names

        display_menu.display_title_and_infos(self.title, self.information)

        choice = "input_stock"

        while True:
            match choice:

                case "input_stock":
                    form_filled = display_menu.display_form(search_form_names, stock_actions)
                    if form_filled:
                        choice = stock_actions.stock_search(token)
                    else:
                        choice = "options"

                case "several_stocks":
                    stock_information = stock_actions.stock_list
                    display_menu.display_title_and_infos(self.title_stock, stock_information)
                    choice = "input_stock"

                case "single_stock":
                    form_filled = display_menu.display_form(trade_form_names, stock_actions)
                    if form_filled:
                        display_menu.display_dic(stock_actions.to_dict())
                        choice = display_menu.display_options(self.options_make_trade)
                    else:
                        choice = "options"

                case "no_stocks":
                    display_menu.display_info(stock_actions.stock_information)
                    choice = "options"

                case "make_trade":
                    success = stock_actions.stock_trade(token)
                    if success:
                        if type(stock_actions.response) is str:
                            display_menu.display_info(stock_actions.response)
                        else:
                            display_menu.display_dic_in_dic(stock_actions.response)
                    else:
                        # trade = "Handel konnte nicht abgechlossen werden."
                        display_menu.display_title_and_infos(self.title, stock_actions.response)
                    choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options)
                    return choice

                case _:
                    display_menu.display_info("Programmfehler im Menü")
                    return "start"
