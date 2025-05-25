from passlib.context import CryptContext
from datetime import datetime, timedelta

from utilities import ValidationError, bank_account_encode, time_check
from repository import insert_customer
from schemas import AccountForm


class CustomerRegistration:
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

    def fill_in(self, account_form: AccountForm):
        errors = []

        for key, value in account_form.model_dump().items():
            try:
                setattr(self, key, value)

            except Exception as e:
                errors.append(f"Fehlerhafte Eingabe für {key}: {e}")

        if errors:
            raise ValidationError(errors)

    # last name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, input):
        if len(input) >= 2:
            self._last_name = input
        else:
            raise ValidationError("mindestens zwei Zeichen")

    # first name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, input):
        if len(input) >= 2:
            self._first_name = input
        else:
            raise ValidationError("mindestens zwei Zeichen")

    #  street
    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, input):
        if len(input) >= 2:
            self._street = input
        else:
            raise ValidationError("mindestens zwei Zeichen")

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
                    raise ValidationError("Die Hausnummer muss eine Zahl beinhalten")
        else:
            raise ValidationError("mindestens ein Zeichen")

    # city
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, input):
        if len(input) >= 2:
            self._city = input
        else:
            raise ValidationError("mindestens zwei Zeichen")

    # zip code
    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, input):
        try:
            input = int(input)
            if input >= 1067 and input <= 99998:
                self._zip_code = input
            else:
                raise ValidationError("ungültige Postleitzahl")

        except ValueError:
            raise ValidationError("ungültige Postleitzahl")

    # birthday
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, input):
        input = input.strip()
        test = time_check(input)
        if test:
            today = datetime.today()
            adult_date = today - timedelta(days=18*365)
            birthday = datetime.strptime(input, "%d.%m.%Y")
            if birthday <= adult_date:
                self._birthday = input
            else:
                raise ValidationError("unter 18")
        else:
            raise ValueError("Bitte das Format tt.mm.jjjj beachten")

    # email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, input):
        char_a = "@"
        char_dot = "."
        if char_a in input and char_dot in input:
            self._email = input
        else:
            raise ValidationError("ungültige E-Mail Adressse")

    # phone number
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, input: str):
        if len(input) >= 11 and len(input) <= 13:
            for number in input:
                if not number.isdigit():
                    raise ValidationError("Telfeonnummer darf nur Zahlen beinhalten")

            self._phone_number = input

        else:
            raise ValueError("ungülitge Länge")

    # reference account
    @property
    def reference_account(self):
        encode = bank_account_encode(self._reference_account)
        return encode

    @reference_account.setter
    def reference_account(self, input):
        if len(input) >= 2:
            self._reference_account = input
        else:
            raise ValidationError("mindestens zwei Zeichen")

    # balance
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
                raise ValidationError("Bitte eine positive Zahl eingeben")
        except ValueError:
            raise ValueError("Bitte eine positive Zahl eingaben")

    # passwort
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, input):
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

                password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
                self._password = password_context.hash(input)
            else:
                raise ValidationError("Passwort entspricht nicht den Sicherheitsstandart")
        else:
            raise ValidationError("Mindestens zwölf Zeichen")

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
            "fin_amount": self.fin_amount,
            "password": self.password
        }

    def insert_db(self):
        as_dic = self.to_dict()
        insert_customer(as_dic)
