from .stock_actions import StockActions


class Watchlist(StockActions):
    def __init__(self):

        self.type_of_editing = None
        self.column_names = {"isin": "ISIN",
                             "company_name": "Unternehmen",
                             "price": "Preis",
                             "current_price": "Aktueller Preis",
                             "performance": "Kursentwicklung",
                             "date": "Datum"}

        super().__init__()

    def get_watchlist(self, token):
        url_part = "watchlist/"
        self.success, self.response = self.server_request.get_without_parameters(url_part, token)

    def edit_watchlist(self, token):
        url_part = "editingwatchlist/"
        to_transmit = {"isin": self.isin}

        if self.type_of_editing:
            self.success, self.response = self.server_request.make_post_request(url_part, token, to_transmit)
        else:
            self.success, self.response = self.server_request.make_delete_request(url_part, token, to_transmit)
