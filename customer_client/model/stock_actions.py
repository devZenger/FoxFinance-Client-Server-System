from service import ServerRequest


class StockActions:
    def __init__(self):

        self.server_request = ServerRequest()

        self._search_term = ""
        self.stock_list = ""
        self.stock_information = None

        self.response = None

        self.search_form_names = {"search_term": "ISIN, Symbol oder Name"}

        self.trade_form_names = {"amount": "Anzahl",
                                 "type_of_action": "Kaufen oder Verkaufen"}

        self.isin = ""
        self.stock_name = ""
        self._amount = 0
        self._type_of_action = ""
        self._type_of_action_en = ""

    @property
    def search_term(self):
        return self._search_term

    @search_term.setter
    def search_term(self, input):
        if len(input) >= 2:
            self._search_term = input
        else:
            raise ValueError("Mindestens zwei Zeichen")

    @property
    def type_of_action(self):
        return self._type_of_action

    @property
    def type_of_action_en(self):
        return self._type_of_action_en

    @type_of_action.setter
    def type_of_action(self, input: str):
        input = input.lower()

        if input == "kaufen" or input == "kauf" or input == "buy":
            self._type_of_action = "kaufen"
            self._type_of_action_en = "buy"
        elif input == "verkaufen" or input == "verkauf" or input == "sell":
            self._type_of_action = "verkaufen"
            self._type_of_action_en = "sell"
        else:
            raise ValueError("Fehler")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, input):
        input = int(input)
        if input > 0:
            self._amount = input
        else:
            raise ValueError("Fehler, keine ganze Zahl größer 0")

    def match_server_response(self, input: dict):

        data_dict = {}

        dic_info = {"Name": f"{input["stocks_row"]["company_name"]}",
                    "Symbol": f"{input["stocks_row"]["ticker_symbol"]}",
                    "ISIN": f" {input["stocks_row"]["isin"]}"}

        data_dict["Informationen"] = dic_info

        dic_lastest_day = {"Datum": f"{input["latest_day"]["date"]}",
                        "Öffnungskurs": f"{input["latest_day"]["open"]:.2f} €",
                        "höchster Kurs": f"{input["latest_day"]["high"]:.2f} €",
                        "tiefster Kurs": f"{input["latest_day"]["low"]:.2f} €",
                        "Schlusskurs": f"{input["latest_day"]["close"]:.2f} €"}

        data_dict["Aktuellster Handelstag"] = dic_lastest_day

        dic_six_months = {"Kurs": f"{input["6 months"]["price"]:.2f} €",
                        "Veränderung": f"{input["6 months"]["performance"]:.2f} %"}

        data_dict["Performance über 6 Monate"] = dic_six_months

        dic_one_year = {"Kurs": f"{input["1 years"]["price"]:.2f} €",
                        "Veränderung": f"{input["1 years"]["performance"]:.2f} %"}

        data_dict["Performance über ein Jahr"] = dic_one_year

        dic_two_year = {"Kurs": f"{input["2 years"]["price"]:.2f} €",
                        "Veränderung": f"{input["2 years"]["performance"]:.2f} %"}

        data_dict["Performance über zwei Jahre"] = dic_two_year

        return data_dict

    def stock_search(self, token):
        url_part = "stocksearch/"

        get_data, response = self.server_request.get_with_parameters(url_part, token, self.search_term)

        if get_data is False:
            return (f"\tFehler, {self.response.status_code}\n"
                    "\tÜberprüfen Sie die Verbindung")
        else:
            results = {}
            results = response

            if results == "Die Aktien konnte nicht gefunden werden":
                self.stock_information = results
                return "no_stocks"

            elif len(results) > 1:
                result_str = "ISIN\t\t | Ticker Symbol | Firmenname\n"

                for result in results.values():

                    result_str = f"{result_str}\t"
                    for value in result.values():
                        if len(value) < 4:
                            add = "\t"
                        else:
                            add = ""

                        result_str = f"{result_str}{value}{add}\t | "

                    result_str = result_str[:-2]
                    result_str = f"{result_str}\n"

                self.stock_list = f"{result_str}\n\tEs wurden mehrere gefunden"

                return "several_stocks"

            else:
                self.isin = results["one"]["latest_day"]["isin"]
                self.stock_name = results["one"]["stocks_row"]["company_name"]

                self.stock_information = self.match_server_response(results["one"])

                return "single_stock"

    def to_dict(self):
        return {"Unternehmen": f"{self.stock_name}",
                "ISIN": f"{self.isin}",
                "Anzahl": f"{self.amount}",
                "Kaufen oder Verkaufen": f"{self.type_of_action}"}

    def stock_trade(self, token):

        url_part = "tradestocks"

        order = {"isin": self.isin,
                 "amount": self.amount,
                 "transaction_type": self.type_of_action_en}

        success, self.response = self.server_request.make_post_request(url_part, token, order)

        return success
