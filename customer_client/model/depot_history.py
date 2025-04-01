import requests
from datetime import datetime, timedelta

from .server_request import ServerRequest


class DepotHistory:

    def __init__(self, token):

        self.server_request = ServerRequest(token)
        self.status_code = None

        self._start_time = None
        self._end_time = None

        self.form_names = {"start_time":"Startdatum (jjjj-mm-tt) ",
                           "end_time":"Enddatum (jjjj-mm-tt) "}

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, input:str):
        print(f"input = {input}")
        split = input.split("-")
        print(f"split= {len(split[0])}    split= {split[0]}")
        if len(split[0]) == 4 and len(split[1])==2 and len(split[2])==2:
            print(f"start time. {input}")
            self._start_time=input
        else:
            raise ValueError("Eingabeformat muss yyyy-mm-dd entsprechen")

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, input: str):
        split = input.split("-")

        if len(split[0]) == 4 and len(split[1])==2 and len(split[2])==2:
            print(f"end_time = {input}")
            self._end_time = input
        else:
            raise ValueError("Eingabeformat muss yyyy-mm-dd entsprechen")

    def get_all_stocks(self):

        url_part = "depotoverview/"

        success, self.response = self.server_request.get_without_parameters(url_part)

        return success

    def get_transaction_by_timespan(self):

        url_part = "pasttransactions/"

        success, self.response = self.server_request.get_with_parameters(url_part, self.start_time, self.end_time)

        return success

    #test und dann löschen
    def _get_transaction_by_timespan(self):

        url_depot = f'{url_server_depot}pasttransactions/{self.start_time}/{self.end_time}/'
        print(f"url get transaction: {url_depot}")
        headers = {"Authorization": f"Bearer {self.token['access_token']}"}

        self.response = requests.get(url_depot, headers=headers)

        self.status_code =  self.response.status_code
        self.response = self.response.json()

        if self.status_code == 200:
            print(self.status_code)
            return True

        else:
            print(self.status_code)
            return False

    def get_last_three_months(self):

        today = datetime.today()
        three_months_ago = today - timedelta(days=90)
        print(today)
        print(three_months_ago)
        self.end_time = today.strftime("%Y-%m-%d")
        self.start_time = three_months_ago.strftime("%Y-%m-%d")

        result = self.get_transaction_by_timespan()

        return result

    def get_last_twelve_months(self):

        today = datetime.today()
        three_months_ago = today - timedelta(days=365)

        print(today.strftime("%Y-%m-%d"))

        self.start_time = today.strftime("%Y-%m-%d")
        self.end_time = three_months_ago.strftime("%Y-%m-%d")

        result = self.get_transaction_by_timespan()

        return result
