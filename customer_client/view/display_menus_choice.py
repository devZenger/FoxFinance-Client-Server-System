

class DisplayMenuChoice:
    line = "-" * 80
    def __init__(self, menu_title, menu_points, info = ""):
        self.menu_title = menu_title
        self.menu_points = menu_points
        self.info = info
        
    def execute(self):
         while True:
            self.display_title()
            
            
            self.display_info()
            
            self.display_option()
        
    
    def display_title(self):
        print(self.line)
        print(f"\t{self.menu_title}")
        print(self.line)
    
    def display_info(self):
        if len(self.info) > 1:
            print(f"\t{self.info}")
            print(self.line)
        
    def display_option(self):
        count = 1
        for key in self.menu_points:
            print(f"\t{key}")
            count += 1
        print(self.line)
        choice = input(f"\tbitte Menüpunkt auswählen (1-{count-1} eingeben): ")
        test = False
        for key in self.menu_points:
            if choice in key:
                self.menu_points[key](self)
                test = True
                
        if test is False:
            print("Fehlerhafte eingabe")
       
