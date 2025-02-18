class Display:
    def show(self, input):
        print(input)


class MenuDisplayChoice:
    def __init__(self, menu_title, menu_points):
        self.menu_title = menu_title
        self.menu_points = menu_points

    def show(self):
        while True:
            print(self.menu_title)
            count = 1
            for key in self.menu_points:
                print(f"{key}")
                count += 1
            choice = input(f"bitte Menüpunkt auswählen (1-{count-1} eingeben): ")
            test = False
            for key in self.menu_points:
                if choice in key:
                    self.menu_points[key](self)
                    test = True
            if test is False:
                print("Fehlerhafte eingabe")

class MenuDisplayForm:
    def __init__(self, menu_title, menu_points):
        self.menu_title = menu_title
        self.menu_points = menu_points

    def execute_form(self):
        print(self.menu_title)
        for key in self.menu_points:
            self.menu_points[key] = input(f"{key}")
        return self.menu_points







class MenuBase:
   
    def __init__(self, title, menupoints, display_choice, infos = ""):
        self.menuhead = title
        self.menupoints = menupoints
        self.display_choice = display_choice
        self.infos = infos
    
    
    def show_menu(self):
        self.display_choice.show(self.menuhead)
        
        
  
  

class MainMenu(MenuBase):
    menu_title = "Hauptmenü"
    
    def example_portfolio(self):
        print("Beispieldepot in Bearbeitung")

    def create_account(self):
        print("Konto erstellen")

    def login(self):
        login = Login()
        login.login_check()

    def information(self):
        information = Information()
        information.run()

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
        super().__init__(self.menu_title, self.menu_points)
  
    def run(self):
        self.execute_choice()
    

  
  
  
  
        


start = MenuBase("test", "tes2t", Display() )
start.show_menu()
    
