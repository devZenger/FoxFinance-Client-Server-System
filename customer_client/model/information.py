import requests


class Information:
    def __init__(self, token):

        self.token = token
        self.form_names = {"search_term":"Informaton suchen :"}
        self.test = "test"

        self.search_term = None
        self.company_name = None
        self.ticker_symbol = None
        self.isin = None
        self.stock_data = None

    def get_information(self):

        url = 'http://127.0.0.1:8000/depot/information/'
        print(self.token)
        headers = { "Authorization": f"Bearer {self.token['access_token']}"}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print ("Empfangen:", response.json())
            print("Informationen für alle")

        else:
            print("Fehler", response.status_code)

        return True
