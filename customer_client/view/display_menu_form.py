from .display_menus_choice import DisplayMenuChoice


class DisplayMenuForm(DisplayMenuChoice):
    def __init__(self, menu_title, menu_points, form_names, to_fill, info=""):
        self.form_names = form_names
        self.to_fills = to_fill
        super().__init__(menu_title, menu_points, info)
    
    
    def execute(self):
        self.display_title()
        self.display_info()
        
        self.display_form()
        
        self.display_option()
    
    
    def display_form(self):
        for key, value in self.form_names.items():
            while True:
                try :
                    user_input = input(f"\t{value} eingeben: ")
                    setattr(self.to_fills, key, user_input)
                    break
                except Exception as e:
                    print(f"Fehlerhafte eingabe: {e}")
        print(self.line)
                    


        print("Bitte Eingaben überprüfen1")
        for key, value in self.form_names.items():
            print(f"\t{value}: {getattr(self.to_fills, key)}")
        


        

        





        