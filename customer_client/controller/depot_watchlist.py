from view import Display
from model import Watchlist


class DepotWatchlist:
    def __init__(self, token):

        self.watchlist = Watchlist(token)

        self.title = "Markliste"
        self.title_stock = "Welche Aktie"
        self.information = "Dezeit nur von DAX Unternehmen möglich"

        self.options = {"1. Aktie hinzufürgen": "add_stock",
                        "2. Aktie entfernen": "remove_stock",
                        "3. Übersicht erneuern": "start",
                        "4. zurück": "discontinue"}

    def run(self):
        display_menu = Display()

        display_menu.display_title_and_infos(self.title, self.information)

        choice = "start"

        while True:
            match choice:

                case "start":
                    self.watchlist.get_watchlist()

                    if self.watchlist.success:
                        display_menu.display_table(self.watchlist.response,
                                                   self.watchlist.column_names)
                    else:
                        display_menu.display_info(self.watchlist.response)

                    choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options)

                case "add_stock":
                    self.watchlist.type_of_editing = True
                    choice = "search_stock"

                case "remove_stock":
                    self.watchlist.type_of_editing = False
                    choice = "search_stock"

                case "search_stock":
                    form_filled = display_menu.display_form(self.watchlist.search_form_names,
                                                            self.watchlist)
                    if form_filled:
                        choice = self.watchlist.stock_search()
                    else:
                        choice = "options"

                case "several_stocks":
                    display_menu.display_title_and_infos(
                        self.title_stock, self.watchlist.stock_list)
                    choice = "search_stock"

                case "single_stock":
                    self.watchlist.edit_watchlist()
                    if self.watchlist.success:
                        display_menu.display_info(
                            f"{self.watchlist.isin} wurde hinzugefügt")
                    else:
                        display_menu.display_info(
                            f"EIn Fehler trat auf: {self.watchlist.response}")
                    choice = "start"

                case "discontinue":
                    return "start"

                case _:
                    choice = "options"
