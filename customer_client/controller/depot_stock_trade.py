
from view import DisplayMenuInput2
from model import StockActions



class DepotStockTrade:
    def __init__(self, token, options):
        self.title="Aktienhandel"
        
        self.title2="Welche Aktie: "
       
        self.information="Derzeit nur von DAX Unternehmen möglich"
        self.token=token
        
        self.options = options
        
        self.options_make_trade ={"1. Handel abschließen":"make_trade", "2. Abrechen":"options"}
        
        
    
    
    def run(self, isin=""):
        
        
        
        display_menu = DisplayMenuInput2()
        self.stock_actions = StockActions(self.token)
        
        search_form_names = self.stock_actions.search_form_names
        trade_form_names = self.stock_actions.trade_form_names
     
        
        display_menu.execute(self.title, self.information)
        
        if isin == "":           
            choice = "input_stock"
        else:
            choice = "single_stock"
        
        while True:
            match choice:
                
                case "input_stock":
                    choice = display_menu.execute_form(search_form_names, self.stock_actions)
                    
                case "form_filled":
                    choice = self.stock_actions.stock_search()
                    
                
                case "several_stocks":
                    self.stock_information=self.stock_actions.stock_list
                    display_menu.execute(self.title2, self.stock_information)
                    choice = "input_stock"
                
                case "single_stock":
                    display_menu.execute_form(trade_form_names, self.stock_actions)
                    display_menu.execute_filled_form(self.stock_actions.form_names)
                    
                    choice= display_menu.excute_options(self.options_make_trade)
                
                case "no_stocks":
                    title_no_stocks="Ergebnis"
                    no_stocks = "Die Aktie konnte nicht gefunden werden"
                    display_menu.execute(title_no_stocks, no_stocks)
                    choice="options"
                    
                    
                case "make_trade":
                    response = self.stock_actions.stock_trade()
                    display_menu.execute(self.title, response)
                    
                    choice="options"
                        
                    
                    
                    
                
                case "options":
                    print("debug options")
                    choice = display_menu.excute_options(self.options)
                
  
                
                case _:
                    return choice