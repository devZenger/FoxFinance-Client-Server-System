from .base_history import BaseHistory


class FinancialHistory(BaseHistory):

    def __init__(self):

        self.column_names = {"fin_transaction_date": "Datum",
                             "fin_transaction_type": "Art der T.",
                             "fin_amount": "Betrag",
                             "bank_account": "Bankkonto"}

        super().__init__('pastfinancialtransactions/')

    def get_actual_balance(self, token):

        url_part = 'current_balance/'

        status, self.response = self.server_request.get_without_parameters(url_part, token)

        if status:
            current_balance = str(round(self.response["actual_balance"], 2))
            self.response = f"AKtueller Kontostand: {current_balance} EUR"

        return status

    def get_last_three_months(self, token):

        self.timespan_for_x_days(days=90)

        result = self.get_information_by_timespan(token)

        return result

    def get_last_twelve_months(self, token):

        self.timespan_for_x_days(days=365)

        result = self.get_information_by_timespan(token)

        return result
