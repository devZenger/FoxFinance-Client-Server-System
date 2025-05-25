from service import ServerRequest

from .financial_history import FinancialHistory


class BankTransfer:
    def __init__(self, token):
        self.token = token
        self._fin_amount = 0.0
        self._transaction_type = ""
        self._usage = ""

        self.form_names = {"fin_amount": "Betrag (. statt ,) ",
                           "transaction_type": "Einzahlen oder Auszahlen ",
                           "usage": "Verwendungszweck "}

    @property
    def fin_amount(self):
        return self._fin_amount

    @fin_amount.setter
    def fin_amount(self, input: str):
        input = input.strip()
        if "," in input:
            input = input.replace("", ","".")

        try:
            input = float(input)
        except ValueError:
            raise ValueError("Fehlerhafte Eingabe")

        if input >= 0:
            self._fin_amount = input
        else:
            raise ValueError("Mindestens 1 Cent")

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, input: str):

        input = input.lower().strip()

        if input == "einzahlen" or input == "deposit":
            self._transaction_type = "einzahlen"
        elif input == "auszahlen" or input == "withdrawal":
            self._transaction_type = "auszahlen"
        else:
            raise ValueError("Fehlerhafte Eingabe")

    @property
    def transaction_type_en(self):
        if self.transaction_type == "einzahlen":
            return "deposit"
        elif self.transaction_type == "auszahlen":
            return "withdrawal"
        else:
            raise ValueError("Fehlende Eingabe")

    @property
    def usage(self):
        return self._usage

    @usage.setter
    def usage(self, input):

        self._usage = input

    def actual_balance(self):
        balance = FinancialHistory(self.token)
        balance.get_actual_balance()
        result = balance.response
        del balance
        return result

    def make_transfer(self):
        url_part = 'banktransfer/'

        server_request = ServerRequest(self.token)

        to_transmit = {"fin_amount": self.fin_amount,
                       "transfer_type": self.transaction_type_en,
                       "usage": self.usage}

        self.success, response = server_request.make_post_request(
            url_part, to_transmit)

        if self.success:
            response = response["row_result0"]

            if response["fin_transaction_type_id"] == 1:
                transaction_type = "einzahlen"
            elif response["fin_transaction_type_id"] == 2:
                transaction_type = "auszahlen"
            else:
                transaction_type = "Fehler"

            transfer_data = {"Bankkonto": f"{response["bank_account"]}",
                             "Betrag": f"{response["fin_amount"]} Euro",
                             "Verwendungszweck": f"{response["usage"]}",
                             "T.Art": f"{transaction_type}",
                             "Datum": f"{response["fin_transaction_date"]}"
                             }

            transfer = {"Überweisung": transfer_data}

            return True, transfer
        else:
            return False, response
