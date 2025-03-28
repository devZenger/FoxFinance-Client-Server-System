from .utility import make_table, make_list_from_dic

class DisplayMenu:
    line = "-" * 90 
    #def __init__(self, title):
    #    self.title = title   

    def display_title(self, title):
        print(self.line)
        print(f"\t{title}")
        print(self.line)
    
    def display_info(self, info):
            print(f"\t{info}")
            print(self.line)
    
    def display_title_and_infos(self, title, info):
        self.display_title(title)
        self.display_info(info)
        
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
                        print("")
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
    
    def display_table(self, input:dict, column_names:dict):
        transform_input= make_table(input, column_names)
        
        for transform in transform_input:
            print(f"\t{transform}")
        
        print("")
        print(self.line)
        

    def display_list(self, input:dict, listpoints:dict):
        
        make_list_from_dic(input, listpoints)
        print("")
        for k,v in listpoints.items():
            print(f"\t{k}:{input[v]}")
        print("")
        print(self.line)