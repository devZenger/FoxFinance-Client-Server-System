from passlib.context import CryptContext

from utilitys import bank_account_encode 
from repository import insert_customer
from schemas import AccountForm

from .utility import (time_check_two,
                      email_check,
                      password_check,
                      house_number_check,
                      phone_number_check,
                      age_check)


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
                print(f"Fehlerhafte eingabe für {key}: {e}")
                errors.append(f"Fehlerhafte eingabe für {key}: {e}")

        if errors:
            raise Exception(errors)

    # last name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, input):
        if len(input) >= 2:
            self._last_name = input
        else:
            raise ValueError("mindestens zwei Zeichen")

    # first name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, input):
        if len(input) >= 2:
            self._first_name = input
        else:
            raise ValueError("mindestens zwei Zeichen")

    #  street
    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, input):
        if len(input) >= 2:
            self._street = input
        else:
            raise ValueError("mindestens zwei Zeichen")

    # house number
    @property
    def house_number(self):
        return self._house_number

    @house_number.setter
    def house_number(self, input):
        if len(input) >= 1:
            check = house_number_check(input)
            if check:
                self._house_number = input
            else:
                raise ValueError("Die Hausnummer muss eine Zahl beinhalten")
        else:
            raise ValueError("mindestens ein Zeichen")

    # city
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, input):
        if len(input) >= 2:
            self._city = input
        else:
            raise ValueError("mindestens zwei Zeichen")

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
                raise ValueError("ungültige Postleitzahl")

        except ValueError:
            raise ValueError("ungültige Postleitzahl")

    # birthday
    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, input):
        input = input.strip()
        test = time_check_two(input)
        if test:
            test = age_check(input)
            if test:
                self._birthday = input
            else:
                raise ValueError("unter 18")
        else:
            raise ValueError("Bitte das Format tt.mm.jjjj beachten")

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
            raise ValueError("ungültige E-Mail Adressse")

    # phone number
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, input):
        if len(input) >= 11 and len(input) <= 13:
            test = phone_number_check(input)
            if test:
                self._phone_number = input
            else:
                raise ValueError("Telfeonnummer darf nur Zahlen beinhalten")
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
            raise ValueError("mindestens zwei Zeichen")

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
                raise ValueError("Bitte eine positive Zahl eingeben")
        except ValueError:
            raise ValueError("Bitte eine positive Zahl eingaben")

    # passwort
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, input):
        if len(input) >= 12:
            test, error = password_check(input)
            if test:
                password_context = CryptContext(schemes=["bcrypt"],
                                                deprecated="auto")
                self._password = password_context.hash(input)
            else:
                raise ValueError("Passwort muss mindestens "
                                 f"{error} enthalten")
        else:
            raise ValueError("Mindestens zwölf Zeichen")

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

        try:
            insert_customer(as_dic)

        except Exception as e:
            print(e)
            raise ValueError(e)
