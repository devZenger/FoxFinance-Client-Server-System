from .server_request import ServerRequest
from .utility import time_check_two, email_check
class RegistrationForm:
    def __init__(self):
        self._last_name = ""
        self._first_name = ""
        self._street = ""
        self._house_number = ""
        self._zip_code = ""
        self._city = ""
        self._birthday = ""
        self._email = ""
        self._phone_number = ""
        self._reference_account = ""
        self._fin_amount = 0.0
        self._password = ""

        self.response = None

        self.form_names = {
            "last_name": "Familiennamen",
            "first_name": "Vorname",
            "street": "Straße (ohne Hausnummer)",
            "house_number": "Hausnummer",
            "city": "Stadt",
            "zip_code": "Postleitzahl",
            "birthday": "Geburtstag (tt.mm.jjjj)",
            "email": "E-Mail Adresse",
            "phone_number": "Handynummer",
            "reference_account": "Referenzkonto",
            "fin_amount": "Startgeld einzahlen",
            "password": "Passwort"
        }

    # last name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, input: str):
        if len(input) >= 2:
            self._last_name = input
        else:
            raise ValueError("Mindestens zwei Zeichen")

    # first name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, input: str):
        if len(input) >= 2:
            self._first_name = input
        else:
            raise ValueError("Mindestens zwei Zeichen")

    #  street
    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, input: str):
        if len(input) >= 2:
            self._street = input
        else:
            raise ValueError("Mindestens zwei Zeichen")

    # house number
    @property
    def house_number(self):
        return self._house_number

    @house_number.setter
    def house_number(self, input: str):
        if len(input) >= 1:
            self._house_number = input
        else:
            raise ValueError("Mindestens zwei Zeichen")

    # city
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, input: str):
        if len(input) >= 2:
            self._city = input
        else:
            raise ValueError("Mindestens zwei Zeichen")

    # zip code
    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, input: int):
        try:
            input = int(input) 
            if input >= 1067 and input <= 99998:
                self._zip_code = input
            else:
                raise ValueError("Ungültige Postleitzahl")

        except ValueError:
            raise ValueError("Ungültige Postleitzahl")

    # birthday
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, input: str):
        input = input.strip()
        test = time_check_two(input)
        if test:
            self._birthday = input
        else:
            raise ValueError("Fehlerhafte Eingabe, tt.mm.jjjj beachten")

    # email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, input):
        test = email_check(input)
        if test:
            self._email = input
        else:
            raise ValueError("Fehlerfafte Eingabe, ungültige E-Mail Adressse")

    # phone number
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, input):
        if len(input) >= 2:
            self._phone_number = input
        else:
            raise ValueError("Mindestens zwei Zeichen")

    # reference account
    @property
    def reference_account(self):
        return self._reference_account

    @reference_account.setter
    def reference_account(self, input):
        if len(input) >= 2:
            self._reference_account = input
        else:
            raise ValueError("Mindestens zwei Zeichen")

    # start capital / balance
    @property
    def fin_amount(self):
        return self._fin_amount

    @fin_amount.setter
    def fin_amount(self, input):
        try:
            input = float(input)
            if input >= 0:
                self._fin_amount = input
            else:
                raise ValueError("Fehlerhafte Eingabe, bitte positive Zahl eingeban")
        except ValueError:
            raise ValueError("Fehlerhafte Eingabe, bitte eine Zahl eingaben")

    # passwort
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, input: str):
        if len(input) >= 2:
            self._password = input
        else:
            raise ValueError("Mindestens zwei Zeichen")

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "street": self.street,
            "house_number": self.house_number,
            "zip_code": self.zip_code,
            "city": self.city,
            "birthday": self.birthday,
            "email": self.email,
            "phone_number": self.phone_number,
            "reference_account": self.reference_account,
            "fin_amount": self._fin_amount,
            "password": self.password
        }

    def post_registration_form(self):

        to_transmit = self.to_dict()

        server_request = ServerRequest()

        url_part = "create_costumer_account/"

        success, self.response = server_request.make_post_request(url_part,
                                                                  to_transmit)

        del server_request

        return success
