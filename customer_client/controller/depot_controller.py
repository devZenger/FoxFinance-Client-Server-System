import sys
from view import DisplayMenuOption

from .depot_start_menu import DepotStartMenu
from .depot_stock_search import DepotStockSearch
from .depot_informationen import DepotInformation
from .depot_stock_trade import DepotStockTrade
from .depot_overview import DepotOverview
from .depot_financial_overview import AccountOverview
from .depot_bank_transfer import DepotBankTransfer


class DepotControl:
    def __init__(self, token):
        self.token = token
        self.headers = { "Authorization": f"Bearer {self.token['access_token']}"}
        
        self.options ={"1. Depot Übersicht": "depot_overview",
                      "2. Aktien suche":"stock_search",
                      "3. Aktien handeln": "stock_trade",
                      "4. Kontoübersicht":"account_overview",
                      "5. Geld ein-/auszahlen":"bank_transaction",
                      "6. Informationen": "information",
                      "7. Abmelden":"loggout",
                      "8. Abmelden und benden":"loggout_and_exit"}
        
    def run(self):
        
        choice = "start"
        
        while True:
            
            match choice:
                    
                case "start":
                    depot_menu_start = DepotStartMenu(self.token, self.options)
                    choice = depot_menu_start.run()
                
                case "depot_overview":
                    depot_overview = DepotOverview(self.token)
                    depot_overview.run()
                    choice = "start"
                    
                case "stock_search":
                    stock_search = DepotStockSearch(self.token, self.options)
                    choice, isin = stock_search.run()
                      
                case "stock_trade":                    
                    stock_trade = DepotStockTrade(self.token, self.options)
                    choice = stock_trade.run()

                case "account_overview":
                    account_overview = AccountOverview(self.token)
                    account_overview.run()
                    choice = "start"
                
                case "bank_transaction":
                    bank_transaction = DepotBankTransfer(self.token, self.options)
                    choice = bank_transaction.run()
                    choice = "start"
                    
                    
                    

                case "information":
                    information = DepotInformation(self.token)
                    information.run()
                    choice = "start"
                    
                case "loggout":
                    del self.token
                    if isinstance(depot_menu_start, DisplayMenuOption):
                        del display_menu
                    
                    return
                
                case "loggout_and_exit":
                    del self.token
                    if isinstance(depot_menu_start, DisplayMenuOption):
                        del display_menu
                    
                    sys.exit(0)
                    
                    