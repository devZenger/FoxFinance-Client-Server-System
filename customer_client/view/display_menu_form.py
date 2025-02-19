from .display_menus_choice import DisplayMenuChoice


class DisplayMenuForm(DisplayMenuChoice):
    def __init__(self, menu_title, menu_points, form_names, to_fill, info=""):
        self.form_names = form_names
        self.to_fill = to_fill
        super().__init__(menu_title, menu_points, info)
    
    
    def execute(self):
        self.display_title()
        
        self.display_info()
        
        self.display_form()
        
        self.display_filled_form()
        
        self.display_option()
    
    
    def display_form(self):
        for key, value in self.form_names.items():
            while True:
                try :
                    user_input = input(f"\t{value} eingeben: ")
                    setattr(self.to_fill, key, user_input)
                    break
                except Exception as e:
                    print(f"\tFehlerhafte eingabe: {e}")
        print(self.line)
                    

    def display_filled_form(self):
        print("\tBitte Eingaben überprüfen")
        for key, value in self.form_names.items():
            print(f"\t{value}: {getattr(self.to_fill, key)}")
        
        print(self.line)
        


        

        





        