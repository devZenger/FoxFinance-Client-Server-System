from datetime import datetime, timedelta

from service import ServerRequest

from .model_utilites import check_date_input, format_time_to_de, format_time_to_en


class DepotHistory:

    def __init__(self):

        self.server_request = ServerRequest()

        self._start_time = ""
        self._start_time_en = ""
        self._end_time = ""
        self._end_time_en = ""

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

    @property
    def start_time_en(self):
        return self._start_time_en

    @start_time.setter
    def start_time(self, input: str):
        input = input.strip()

        check, date, message = check_date_input(input)

        if message == "EN":
            self._start_time_en = date
            self.start_time = format_time_to_de(date)

        elif check:
            self._start_time = date
            self._start_time_en = format_time_to_en(date)
        else:
            raise ValueError(message)

    @property
    def end_time(self):
        return self._end_time

    @property
    def end_time_en(self):
        return self._end_time_en

    @end_time.setter
    def end_time(self, input: str):

        check, date, message = check_date_input(input)

        if message == "EN":
            self._end_time_en = date
            self.start_time = format_time_to_de(date)

        elif check:
            self._end_time = date
            self._end_time_en = format_time_to_en(date)
        else:
            raise ValueError(message)

    def get_all_stocks(self, token):

        url_part = "depotoverview/"

        success, self.response = self.server_request.get_without_parameters(url_part, token)

        return success

    def get_transaction_by_timespan(self, token):

        url_part = "pasttransactions/"

        success, self.response = self.server_request.get_with_parameters(url_part, token,
                                                                         self.start_time,
                                                                         self.end_time)

        return success

    def get_last_thirty_days(self, token):

        today = datetime.today()
        thirty_days_ago = today - timedelta(days=30)

        self.end_time = today.strftime("%Y-%m-%d")
        self.start_time = thirty_days_ago.strftime("%Y-%m-%d")

        result = self.get_transaction_by_timespan(token)

        return result

    def get_last_three_months(self, token):

        today = datetime.today()
        three_months_ago = today - timedelta(days=90)

        self.end_time = today.strftime("%Y-%m-%d")
        self.start_time = three_months_ago.strftime("%Y-%m-%d")

        result = self.get_transaction_by_timespan(token)

        return result
