from datetime import datetime, timedelta

from .server_request import ServerRequest

from .utility import time_check


class FinancialHistory:

    def __init__(self, token):

        self.server_request = ServerRequest(token)

        self._start_time = ""
        self._end_time = ""

        self.form_names = {"start_time": "Startdatum (jjjj-mm-tt) ",
                           "end_time": "Enddatum (jjjj-mm-tt) "}

        self.column_names = {"fin_transaction_date": "Datum",
                             "fin_transaction_type": "Art der T.",
                             "fin_amount": "Betrag",
                             "bank_account": "Bankkonto"}

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, input: str):
        input = input.strip()
        
        check = time_check(input)
   
        if check:
            self._start_time = input
        else:
            raise ValueError("Eingabeformat muss yyyy-mm-dd entsprechen")

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, input: str):
        input = input.strip()
        check = time_check(input)

        if check:
            self._end_time = input
        else:
            raise ValueError("Eingabeformat muss yyyy-mm-dd entsprechen")

    def get_actual_balance(self):

        url_part = 'current_balance/'

        status, self.response = self.server_request.get_without_parameters(
            url_part)
        print(f"get-acutal_balance: self.response: {self.response}")

        if status:
            current_balance = str(round(self.response["actual_balance"], 2))
            self.response = f"AKtueller Kontostand: {current_balance} EUR"

        return status

    def get_fin_transaction_by_timespan(self):

        url_part = 'pastfinancialtransactions/'

        status, self.response = self.server_request.get_with_parameters(
            url_part, self.start_time, self.end_time)

        return status

    def get_last_three_months(self):

        today = datetime.today()
        three_months_ago = today - timedelta(days=90)

        self.end_time = today.strftime("%Y-%m-%d")
        self.start_time = three_months_ago.strftime("%Y-%m-%d")

        result = self.get_fin_transaction_by_timespan()

        return result

    def get_last_twelve_months(self):

        today = datetime.today()
        three_months_ago = today - timedelta(days=365)

        self.end_time = today.strftime("%Y-%m-%d")
        self.start_time = three_months_ago.strftime("%Y-%m-%d")

        result = self.get_fin_transaction_by_timespan()

        return result
