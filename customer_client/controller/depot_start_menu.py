import requests

from view import DisplayMenuOption

from model import url_server

class DepotStartMenu:
    def __init__(self, token, option):
        self.title = "Willkommen in ihren Depot"
        self.token=token
        self.option=option
        
    def run(self):
        
        
        
        headers = { "Authorization": f"Bearer {self.token["access_token"]}"}
        
        url =  'http://127.0.0.1:8000/depot/'
        
        response = requests.get(url, headers=headers)
        
        info = response.json()
        print(f"info: {info}")
        info_sub = info["message"]
        
        display = DisplayMenuOption(self.title, info_sub)
       
        return display.execute(self.option)
        
        
        
        
        
    