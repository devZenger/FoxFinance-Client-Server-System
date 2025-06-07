from service import ServerRequest

from .base_history import BaseHistory


class DepotHistory(BaseHistory):

    def __init__(self):

        # self.server_request = ServerRequest()

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
        super().__init__("pasttransactions/")

    def get_all_stocks(self, token):

        url_part = "depotoverview/"

        success, self.response = self.server_request.get_without_parameters(url_part, token)

        return success

    def get_last_thirty_days(self, token):

        self.timespan_for_x_days(30)

        result = self.get_information_by_timespan(token)

        return result

    def get_last_three_months(self, token):

        self.timespan_for_x_days(90)

        result = self.get_information_by_timespan(token)

        return result
