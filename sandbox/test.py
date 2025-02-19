class Form:
    def __init__(self):
        self._animal = None
        self._age = None
    
    @property
    def animal(self):
        return self._animal
    
    @animal.setter
    def animal(self, input):
        if len(input) > 2:
            self._animal = input
        else:
            raise ValueError("min 2 chars")
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, input):
        if len(input) > 1:
            self._age = input
        else:
            raise ValueError("min 1 chars")



class Display:
    def __init__(self, title, form_name, to_fill, to_fillC):
        self.title = title
        self.formN = form_name
        self.to_fill= to_fill
        self.to_fillC = to_fillC
    
    def display(self):
        print(self.title)
        
        for key, v in self.formN.items():
            while True:
                try :
                    self.to_fill[key] = input(f"{v} eingeben: ")
                    setattr(self.to_fillC, key, self.to_fill[key])
                    break
                except Exception as e:
                    print("Fehlerhafte eingabe: {e}")
        
        print("Eingaben")
        
        
        for k, v in self.to_fillC.__dict__.items():
            print(f"{k} : {v}")
            
        
        
        
        
        
       



        #for key, item in self.form.items():
         #   print("test") 
          #  print(f"{key}: {item}")
        





class MenuBase:
    def __init__(self, display):
        self.display= display
    
    def show(self):
        self.display.display()


class AddAnimal(MenuBase):
    titel = "Aninaml input"
    to_fillC = Form()
    
    form_name ={
        "animal":"Tier",
        "age":"Alter"
    }
    
    to_fill = {
        "animal": None,
        "age": None
    }
    
    def __init__(self):
        super().__init__(Display(self.titel, self.form_name, self.to_fill, self.to_fillC))


  
  
  
    

start = AddAnimal()
start.show()


    
