from .server_request import ServerRequest


class Validation:
    def __init__(self):

        self.server_request = ServerRequest()

        self._validation_number = None

        self.form_name = {"validation_number": "Bitte Aktivierungscode"}

    @property
    def validation_number(self):
        return self._validation_number

    @validation_number.setter
    def validation_number(self, input):
        if len(input) >= 6:
            try:
                self._validation_number = int(input)

            except:
                raise ValueError("Eingabe muss eine ganze Zahl sein")
        else:
            raise ValueError("Mindestens sechs Zahlen")

    def to_dict(self):
        return {"validation_number":self.validation_number}

    def get_activate_code(self, email):
        url_part = "startvalidation/"

        success, code = self.server_request.get_with_parameters(url_part, email)

        if success is True:

            handy = {"line1": "          #",
                     "line2": "          #",
                     "line3": " __________#___",
                     "line4": "/     :::::    \\",
                     "line5": "|  ___________ |",
                     "line6": "| |~       --| |",
                     "line7": f"| |  {code['validation_number']}  | |",
                     "line8": "| |__________| |",
                     "line9": "|              |\n"}

            return True, handy

        else:
            return False, "Kein Aktivierungscode erhalten"

    def send_activate_code(self):

        url_part = "/activateaccount/"
        to_transmit = self.to_dict()

        success, self.response = self.server_request.make_post_request(
            url_part, to_transmit)

        return success
