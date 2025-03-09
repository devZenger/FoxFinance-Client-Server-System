
from abc import ABC, abstractmethod


class DisplayMenuBase(ABC):
    
    line = "-" * 80
 
    @abstractmethod
    def execute(self):
        pass

    def display_title(self):
        print(self.line)
        print(f"\t{self.title}")
        print(self.line)
    
    def display_info(self):
        if len(self.info) > 1:
            print(f"\t{self.info}")
            print(self.line)
    
    
    def display_options(self):
        count = 1
        for key in self.options:
            print(f"\t{key}")
            count += 1
        print(self.line)
        while True:
            choice = input(f"\tbitte Menüpunkt auswählen (1-{count-1} eingeben): ")
            if choice.isdigit() == True:
                test = False
                for key in self.options:
                    if choice in key:
                        return self.options[key]
            
                if test is False:
                    print("\tFehlerhafte eingabe")
            else:
                 print("\tFehlerhafte eingabe")
    
    
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
        return "form_filled"
                    

    def display_filled_form(self):
        print(" ")
        print("\tBitte Eingaben überprüfen:")
        print(self.line)
        for key, value in self.form_names.items():
            print(f"\t{value}: {getattr(self.to_fill, key)}")
        
        print(self.line)
    