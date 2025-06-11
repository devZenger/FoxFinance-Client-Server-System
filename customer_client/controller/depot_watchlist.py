from view import Display
from model import Watchlist


class DepotWatchlist:
    def __init__(self):
        self.title = "Markliste"
        self.title_stock = "Welche Aktie"
        self.information = "Derzeit nur von DAX Unternehmen möglich"

        self.options = {"1. Aktie hinzufürgen": "add_stock",
                        "2. Aktie entfernen": "remove_stock",
                        "3. Übersicht erneuern": "start",
                        "4. Menü verlassen": "discontinue"}

    def run(self, token):
        watchlist = Watchlist()
        display_menu = Display()

        display_menu.display_title_and_infos(self.title, self.information)

        choice = "start"

        while True:
            match choice:

                case "start":
                    watchlist.get_watchlist(token)

                    if watchlist.success:
                        display_menu.display_table(watchlist.response, watchlist.column_names)
                    else:
                        display_menu.display_info(watchlist.response)

                    choice = "options"

                case "options":
                    choice = display_menu.display_options(self.options)

                case "add_stock":
                    watchlist.type_of_editing = True
                    choice = "search_stock"

                case "remove_stock":
                    watchlist.type_of_editing = False
                    choice = "search_stock"

                case "search_stock":
                    form_filled = display_menu.display_form(watchlist.search_form_names, watchlist)
                    if form_filled:
                        choice = watchlist.stock_search(token)
                    else:
                        choice = "options"

                case "several_stocks":
                    display_menu.display_title_and_infos(self.title_stock, watchlist.stock_list)
                    choice = "search_stock"

                case "single_stock":
                    watchlist.edit_watchlist(token)
                    if watchlist.success:
                        display_menu.display_info(f"{watchlist.isin} wurde hinzugefügt")
                    else:
                        display_menu.display_info(f"EIn Fehler trat auf:\n{watchlist.response}")
                    choice = "start"

                case "discontinue":
                    return "start"

                case _:
                    choice = "options"
