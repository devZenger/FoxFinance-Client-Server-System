class MenuBase:
    menu_title = ""
    menu_points = {}

    def __init__(self, menu_title, menu_points):
        self.menu_title = menu_title
        self.menu_points = menu_points

    def execute_choice(self):
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

    def execute_formular(self):
        print(self.menu_title)
        for key in self.menu_points:
            self.menu_points[key] = input(f"{key}")
        return self.menu_points