import requests

from .url import url_server

#class Depot:
    def __init__(self, token):
        self.title="Depot"
        self.token = token
    
    def request_depot(self):
        
        url = f'{url_server}/depot/stocksearch/{self.search_term}'
        
        headers = { "Authorization": f"Bearer {self.token['access_token']}"}
        
        self.response = requests.get(url, headers=headers)
        
        
        
        if self.response.status_code == 200:
            print ("Empfangen:", self.response.json())
            print("suche erfolgreich")
            self.response = self.response.json()
            return True
            
         
        else:
            print("Fehler", self.response.status_code)
            return False