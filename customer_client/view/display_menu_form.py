from .display_menus_choice import DisplayMenuChoice


class DisplayMenuForm(DisplayMenuChoice):
    def __init__(self, menu_title, menu_points, form2, info=""):
        self.form2= form2
        super().__init__(menu_title, menu_points, info)
    
    
    def execute(self):
        self.display_title()
        self.display_info()
        
        self.display_form()
        
        self.display_option()
    
    
    def display_form(self):
        for key in self.form2:
            try :
                self.form2[key] = input(f"{key} eingeben: ")
            except Exception as e:
                print("Fehlerhafte eingabe: {e}")
                self.form2[key] = input(f"{key} eingeben: ")
        
        self.form2.testfunkt(self)



        for key, item in self.form2.items():
            print("test") 
            print(f"{key}: {item}")
        
                
        
        
        
        #return self.form

        

        





        