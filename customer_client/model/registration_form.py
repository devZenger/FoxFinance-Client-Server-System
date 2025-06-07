from datetime import datetime, timedelta

from service import ServerRequest

from .model_utilites import check_date_input, check_email


class RegistrationForm:
    def __init__(self):
        self._last_name = ""
        self._first_name = ""
        self._street = ""
        self._house_number = ""
        self._zip_code = None
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
            raise ValueError("mindestens zwei Zeichen")

    # first name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, input: str):
        if len(input) >= 2:
            self._first_name = input
        else:
            raise ValueError("mindestens zwei Zeichen")

    # street
    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, input: str):
        if len(input) >= 2:
            self._street = input
        else:
            raise ValueError("mindestens zwei Zeichen")

    # house number
    @property
    def house_number(self):
        return self._house_number

    @house_number.setter
    def house_number(self, input: str):
        if len(input) >= 1:
            for inp in input:
                if inp.isdigit():
                    self._house_number = input
                    break
                else:
                    raise ValueError("Hausnummer muss eine Zahl beinhalten")
        else:
            raise ValueError("mindestens ein Zeichen")

    # city
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, input: str):
        if len(input) >= 2:
            self._city = input
        else:
            raise ValueError("mindestens zwei Zeichen")

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
                raise ValueError("ungültige Postleitzahl")

        except ValueError:
            raise ValueError("ungültige Postleitzahl")

    # birthday
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, input: str):
        check, date, message = check_date_input(input)
        if check:
            today = datetime.today()
            adult_date = today - timedelta(days=18*365)

            birthday_obj = datetime.strptime(date, "%d.%m.%Y")
            if birthday_obj <= adult_date:
                self._birthday = date
            else:
                raise ValueError("unter 18")
        else:
            raise ValueError(message)

    # email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, input):
        test = check_email(input)
        if test:
            self._email = input
        else:
            raise ValueError("ungültige E-Mail Adressse")

    # phone number
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, input):
        if len(input) >= 11 and len(input) <= 13:
            for number in input:
                if not number.isdigit():
                    raise ValueError("Telfeonnummer darf nur Zahlen beinhalten")
            self._phone_number = input
        else:
            raise ValueError("ungülitge Länge")

    # reference account
    @property
    def reference_account(self):
        return self._reference_account

    @reference_account.setter
    def reference_account(self, input):
        if len(input) >= 2:
            self._reference_account = input
        else:
            raise ValueError("Fehlerhafte Eingabe, mindestens zwei Zeichen")

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
                raise ValueError("Bitte eine positive Zahl eingeben")
        except ValueError:
            raise ValueError("Bitte eine positive Zahl eingeben")

    # passwort
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, input: str):
        if len(input) >= 12:

            upper = 0
            lower = 0
            special = 0
            numbers = 0

            for char in input:
                if char.isupper() and char.isalpha():
                    upper += 1
                elif char.islower() and char.isalpha():
                    lower += 1
                elif char.isdigit():
                    numbers += 1
                elif not char.isalnum():
                    special += 1

            if upper > 1 and lower > 1 and numbers > 1 and special > 1:
                self._password = input
            else:
                if upper > 1:
                    error = "einen Großbuchstaben"
                if upper > 1:
                    error = "einen Kleinbuchstaben"
                if numbers > 1:
                    error = "eine Zahl"
                if special > 1:
                    error = "ein Sonderzeichen"

                raise ValueError(f"Passwort muss mindestens {error} enthalten")
        else:
            raise ValueError("Fehler, mindestens zwölf Zeichen")

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

        url_part = "create_customer_account/"

        success, self.response = server_request.make_post_request(url_part, token=None, to_transmit=to_transmit)

        del server_request

        return success
