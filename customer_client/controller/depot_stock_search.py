from view import DisplayMenuInput2
from model import StockActions



class DepotStockSearch:
    def __init__(self, token, options):
        self.title="Aktiensuche"
        self.title2="Ergebnisse: "
        self.title3="Ergebnis: "
        self.information="Derzeit nur Dax unternehmen möglich"
        self.token=token
        
        self.stock_information=None
        
        self.options = options
 
    
    
    def run(self):
        display_menu = DisplayMenuInput2()
        self.stock_actions = StockActions(self.token)
        form_names = self.stock_actions.search_form_names
        
        
        display_menu.execute(self.title, self.information)
        
        choice = "stock_search"
        
        while True:
            match choice:
                
                case "stock_search":
                    print("debug start menu")
                    # if form filled choise = "form_filled"
                    choice = display_menu.execute_form(form_names, self.stock_actions)
                    
                case "form_filled":
                    choice = self.stock_actions.stock_search()
                
                case "several_stocks":
                    self.stock_information=self.stock_actions.stock_list
                    display_menu.execute(self.title2, self.stock_information)
                    choice = "options"
                
                case "single_stock":
                    self.stock_information=self.stock_actions.stock_information
                    display_menu.execute(self.title3, self.stock_information)
                    choice="options"
                
                case "options":
                    print("debug options")
                    choice = display_menu.excute_options(self.options)
                
                case "stock_buy":
                    isin =  self.stock_actions.isin
                    return "buy_stocks", isin
                
                case _:
                    return choice, ""
                    
    
    
        
        
        
            
        
        