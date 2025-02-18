from display_menus import display_menu_choice

class MenuBase:
   
    def __init__(self, title, menupoints, display_choice, infos = ""):
        self.menuhead = title
        self.menupoints = menupoints
        self.display_choice = display_choice
        self.infos = infos
    
    
    def show_menu(self):
        self.display_choice.execute_menu(self.menuhead, self.menupoints)
        
        
  
  

class MainMenu(MenuBase):
    menu_title = "Hauptmenü"
    
    def example_portfolio(self):
        print("Beispieldepot in Bearbeitung")

    def create_account(self):
        print("Konto erstellen")

    def login(self):
        print ("Login")

    def information(self):
        print("info")

    def end_programm(self):
        print("Programm beenden")
        exit(0)

    menu_points = {
        "1.Beispieldepot betrachten": example_portfolio,
        "2.Konto erstellen": create_account,
        "3.Login": login,
        "4.Informationen": information,
        "5.beenden": end_programm
        }

    def __init__(self):
        super().__init__(self.menu_title, self.menu_points, display_menu_choice())
  
    
    
    
    
    
    


start = MainMenu()
start.show_menu()