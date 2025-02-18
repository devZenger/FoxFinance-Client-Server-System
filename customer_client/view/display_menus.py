from abc import ABC, abstractmethod


class DisplayMenu(ABC):
    @abstractmethod
    def execute_menu(self, menu_title, menu_points, info, form):
        pass
    

class DisplayMenuChoice(DisplayMenu):
    def execute_menu(self, menu_title, menu_points, info = "", form= None):
        if form is None:
            form = {}
            
        print(f"form länge: {len(form)}")
        while True:
            print(menu_title)
            print(info)
            
            if len(info) > 0:
                print(info)
            
            if len(form) > 0:
                print("test")
                filled_form = self.__show_form(form)
            
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
    
    def __show_form(self, form):
        for key in form:
            try :
                print("test")
                form[key] = input(f"{key} eingeben: ")
            except Exception as e:
                print("Fehlerhafte eingabe: {e}")
                form[key] = input(f"{key} eingeben: ")


        print(" ")
        print("test")
        for key, item in form:   
            print(f"{key}: {item} test")
        
                
        
        
        return form






class DisplayMenuForm(DisplayMenu):
    def execute_menu(self, menu_title, menu_points, form):
        print(menu_title)
        
        for key in menu_points:
            menu_points[key] = input(f"{key}")
        return menu_points
        
