from view import DisplayMenuChoice

from .menu_base import MenuBase

class CustomerStartMenu(MenuBase):
    def __init__(self):
        self.menu_title = "Kundenmenü"
        self.info = "Willkommen"
        
        super().__init__(DisplayMenuChoice())
        
        