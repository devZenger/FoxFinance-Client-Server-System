import requests

from view import DisplayMenuChoice

from .server_url import server_URL
from .menu_base import MenuBase

class InformationMenu(MenuBase):
    def __init__(self):
        self.menu_title= "Information Menü:"
        self.information = self.get_information()
        self.menu_points = {
            "1. zurück": self.discontinue
             }
        
        super().__init__(DisplayMenuChoice(self.menu_title, self.menu_points, self.information))
        
    def discontinue(self, test = None):
        from .welcome_menu import WelcomeMenu
        start = WelcomeMenu()
        start.show()
        
    def get_information(self):
        url = f"{server_URL}/information/"
        response = requests.get(url)
        data = response.json()  
        return data["message"]
