from .stock_actions import StockActions
from .server_request import ServerRequest


class Watchlist(StockActions):
    def __init__(self, token: str):

        self.server_request = ServerRequest(token)
        self.type_of_editing = None
        self.column_names = {"isin": "ISIN",
                             "company_name": "Unternehmen",
                             "price": "Preis",
                             "current_price": "Aktueller Preis",
                             "performance": "Kursentwicklung",
                             "date": "Datum"}

        super().__init__(token)

    def get_watchlist(self):
        url_part = "watchlist/"
        self.success, self.response = self.server_request.get_without_parameters(url_part)

    def edit_watchlist(self):
        url_part = "editingwatchlist/"
        to_transmit = {"isin": self.isin}

        if self.type_of_editing:
            to_transmit["transaction_type"] = True
        else:
            to_transmit["transaction_type"] = False

        self.success, self.response = self.server_request.make_post_request(
            url_part, to_transmit)
