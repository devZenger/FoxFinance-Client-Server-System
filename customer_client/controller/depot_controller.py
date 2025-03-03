import sys
from view import DisplayMenuOption

from .depot_start_menu import DepotStartMenu


class DepotControl:
    def __init__(self, token):
        self.token = token
        self.option ={"1. Depot Übersicht": "depot overview",
                      "2. Aktien kaufen": "buy stocks",
                      "3. Aktien verkaufen":"sell stocks",
                      "4. Informationen": "information",
                      "5. Abmelden":"loggout",
                      "6. Abmelden und benden":"loggout_and_exit"}
        
    def run(self):
        
        choice = "start"
        
        while True:
            
            match choice:
                    
                case "start":
                    depot_menu_start = DepotStartMenu(self.token, self.option)
                    choice = depot_menu_start.run()
                
                case "depot overview":
                    title ="Depot"
                    info = "in Bearbeitung"
                    display_menu = DisplayMenuOption(title, info)
                    choice = display_menu.execute(self.option)
                
                    
                    
                
                case "buy stocks":
                    title ="Informationen"
                    info = "in Bearbeitung"
                    display_menu = DisplayMenuOption(title, info)
                    choice = display_menu.execute(self.option)
                
                
                case "sell stocks":
                    title ="Informationen"
                    info = "in Bearbeitung"
                    display_menu = DisplayMenuOption(title, info)
                    choice = display_menu.execute(self.option)
                
                case "information":
                    title ="Informationen"
                    info = "in Bearbeitung"
                    display_menu = DisplayMenuOption(title, info)
                    choice = display_menu.execute(self.option)
                
                
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
                    
                    