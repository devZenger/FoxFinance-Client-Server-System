from .utility import make_tabelle

class DisplayMenu:
    
    line = "-" * 80

    def display_title(self, title):
        print(self.line)
        print(f"\t{title}")
        print(self.line)
    
    def display_info(self, info):
            print(f"\t{info}")
            print(self.line)
    
    
    def display_options(self, options):
        count = 1
        for key in options:
            print(f"\t{key}")
            count += 1
        print(self.line)
        while True:
            choice = input(f"\tbitte Menüpunkt auswählen (1-{count-1} eingeben): ")
            if choice.isdigit() == True:
                test = False
                for key in options:
                    if choice in key:
                        return options[key]
            
                if test is False:
                    print("\tFehlerhafte eingabe")
            else:
                 print("\tFehlerhafte eingabe")
    
    
    def display_form(self, form_names:dict, to_fill):
        self.form_names = form_names
        self.to_fill = to_fill
        
        for key, value in form_names.items():
            while True:
                try :
                    user_input = input(f"\t{value} eingeben: ")
                    setattr(self.to_fill, key, user_input)
                    break
                except Exception as e:
                    print(f"\tFehlerhafte eingabe: {e}")
        print(self.line)
        return "form_filled"
                    

    def display_filled_form(self):
        print(" ")
        print("\tBitte Eingaben überprüfen:")
        print(self.line)
        for key, value in self.form_names.items():
            print(f"\t{value}: {getattr(self.to_fill, key)}")
        
        print(self.line)
    
    def display_tabelle(self, input:dict):
        transform_input= make_tabelle(input)
        
        for transform in transform_input:
            print(f"\t{transform}")
        
    