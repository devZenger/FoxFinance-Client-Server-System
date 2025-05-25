import sys

from view import Display

from .depot_start_menu import DepotStartMenu
from .depot_stock_search import DepotStockSearch
from .informationen import AllInformation
from .depot_stock_trade import DepotStockTrade
from .depot_overview import DepotOverview
from .depot_financial_overview import AccountOverview
from .depot_bank_transfer import DepotBankTransfer
from .depot_settings import Settings
from .depot_watchlist import DepotWatchlist


class DepotControl:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token['access_token']}"}

        self.options = {" 1. Depot Übersicht": "depot_overview",
                        " 2. Aktien suche": "stock_search",
                        " 3. Aktien handeln": "stock_trade",
                        " 4. Watchlist": "watchlist",
                        " 5. Kontoübersicht": "account_overview",
                        " 6. Geld ein-/auszahlen": "bank_transfer",
                        " 7. Informationen": "information",
                        " 8. Daten ändern": "settings",
                        " 9. Abmelden": "loggout",
                        "10. Abmelden und benden": "loggout_and_exit"}

        self.depot_menu_start = None
        self.depot_overview = None
        self.stock_search = None
        self.stock_trade = None
        self.watchlist = None
        self.account_overview = None
        self.bank_transaction = None
        self.information = None
        self.settings = None

    def delete_token_instance(self):
        del self.token
        del self.depot_menu_start
        if isinstance(self.depot_overview, Display):
            del self.depot_overview
        if isinstance(self.stock_search, Display):
            del self.stock_search
        if isinstance(self.stock_trade, Display):
            del self.stock_trade
        if isinstance(self.watchlist, Display):
            del self.watchlist
        if isinstance(self.account_overview, Display):
            del self.account_overview
        if isinstance(self.bank_transaction, Display):
            del self.bank_transaction
        if isinstance(self.information, Display):
            del self.information
        if isinstance(self.settings, Display):
            del self.settings

    def run(self):

        choice = "start"
        self.depot_menu_start = DepotStartMenu(self.options, self.token)

        while True:

            match choice:

                case "start":
                    choice = self.depot_menu_start.run()

                case "depot_overview":
                    self.depot_overview = DepotOverview(self.token)
                    self.depot_overview.run()
                    choice = "start"

                case "stock_search":
                    self.stock_search = DepotStockSearch(self.token, self.options)
                    choice = self.stock_search.run()

                case "stock_trade":
                    self.stock_trade = DepotStockTrade(self.token, self.options)
                    choice = self.stock_trade.run()

                case "watchlist":
                    self.watchlist = DepotWatchlist(self.token)
                    choice = self.watchlist.run()

                case "account_overview":
                    self.account_overview = AccountOverview(self.token)
                    choice = self.account_overview.run()

                case "bank_transfer":
                    self.bank_transaction = DepotBankTransfer(self.token, self.options)
                    choice = self.bank_transaction.run()

                case "information":
                    self.information = AllInformation(self.options, self.token)
                    choice = self.information.run()

                case "settings":
                    self.settings = Settings(self.token, self.options)
                    choice = self.settings.run()

                case "loggout":
                    self.delete_token_instance()
                    return

                case "loggout_and_exit":
                    self.delete_token_instance()
                    sys.exit(0)
