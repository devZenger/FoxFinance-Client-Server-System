class MenuBase:
    def __init__(self, display_choice):
        self.display_choice = display_choice
    
    def discontinue(self):
        back = MainMenu()
        back.show()
    
    def show(self):
        self.display_choice.execute()