from abc import ABC, abstractmethod


class display_menu(ABC):
    @abstractmethod
    def execute_menu(self, menu_title, menu_points):
        pass
    

class display_menu_choice(display_menu):
    def execute_menu(self, menu_title, menu_points):
         while True:
            print(menu_title)
            count = 1
            for key in menu_points:
                print(f"{key}")
                count += 1
            choice = input(f"bitte Menüpunkt auswählen (1-{count-1} eingeben): ")
            test = False
            for key in menu_points:
                if choice in key:
                    menu_points[key](self)
                    test = True
            if test is False:
                print("Fehlerhafte eingabe")


class display_menu_form(display_menu):
    def execute_menu(self, menu_title, menu_points):
        print(menu_title)
        for key in menu_points:
            menu_points[key] = input(f"{key}")
        return menu_points
        


