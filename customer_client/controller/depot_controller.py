import sys
from view import DisplayMenuOption

from .depot_start_menu import DepotStartMenu
from .depot_stock_search import DepotStockSearch
from .depot_informationen import DepotInformation
from .depot_stock_trade import DepotStockTrade
from .depot_overview import DepotOverview


class DepotControl:
    def __init__(self, token):
        self.token = token
        self.headers = { "Authorization": f"Bearer {self.token['access_token']}"}
        
        self.option ={"1. Depot Übersicht": "depot_overview",
                      "2. Aktien suche":"stock_search",
                      "3. Aktien handeln": "stock_trade",
                      "5. Informationen": "information",
                      "6. Abmelden":"loggout",
                      "7. Abmelden und benden":"loggout_and_exit"}
        
    def run(self):
        
        choice = "start"
        
        while True:
            
            match choice:
                    
                case "start":
                    depot_menu_start = DepotStartMenu(self.token, self.option)
                    choice = depot_menu_start.run()
                
                case "depot_overview":
                    depot_overview = DepotOverview(self.token)
                    depot_overview.run()
                    choice = "start"
                    
                case "stock_search":
                    stock_search = DepotStockSearch(self.token, self.option)
                    choice, isin = stock_search.run()
                      
                case "stock_trade":                    
                    stock_trade = DepotStockTrade(self.token, self.option)
                    choice = stock_trade.run()

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
                    
                    