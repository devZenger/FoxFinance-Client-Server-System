from datetime import datetime, timedelta

from service import ServerRequest

from .model_utilitys import check_date_input


class DepotHistory:

    def __init__(self, token):

        self.server_request = ServerRequest(token)

        self._start_time = ""
        self._end_time = ""

        self.form_names = {"start_time": "Startdatum (tt.mm.jjjj) ",
                           "end_time": "Enddatum (tt.mm.jjjj) "}

        self.column_names = {"isin": "ISIN",
                             "company_name": "Unternehmen",
                             "amount": "Anzahl",
                             "price_per_stock": "Durchschnittspreis",
                             "actual_price": "Aktueller Preis",
                             "performance": "Kursentwicklung"}

        self.column_names_timespan = {"transaction_id": "T.Nr.",
                                      "transaction_date": "Datum",
                                      "transaction_type": "T. Art.",
                                      "isin": "ISIN",
                                      "company_name": "Unternehmen",
                                      "amount": "Anzahl",
                                      "price_per_stock": "Preis",
                                      "total_order_charge": "Ordergebühren"}

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, input: str):

        check, date, message = check_date_input(input)

        if check:
            self._start_time = date
        else:
            raise ValueError(message)

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, input: str):

        check, date, message = check_date_input(input)

        if check:
            self._end_time = date
        else:
            raise ValueError(message)

    def get_all_stocks(self):

        url_part = "depotoverview/"

        success, self.response = self.server_request.get_without_parameters(url_part)

        return success

    def get_transaction_by_timespan(self):

        url_part = "pasttransactions/"

        success, self.response = self.server_request.get_with_parameters(url_part, self.start_time, self.end_time)

        return success

    def get_last_thirty_days(self):

        today = datetime.today()
        thirty_days_ago = today - timedelta(days=30)

        self.end_time = today.strftime("%Y-%m-%d")
        self.start_time = thirty_days_ago.strftime("%Y-%m-%d")

        result = self.get_transaction_by_timespan()

        return result

    def get_last_three_months(self):

        today = datetime.today()
        three_months_ago = today - timedelta(days=90)

        self.end_time = today.strftime("%Y-%m-%d")
        self.start_time = three_months_ago.strftime("%Y-%m-%d")

        result = self.get_transaction_by_timespan()

        return result
