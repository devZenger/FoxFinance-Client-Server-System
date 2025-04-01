from .server_request import ServerRequest


class LoginForm:
    def __init__(self):
        self._email = None
        self._password = None
        self.response = None

        self.form_names = {"email":"Email Adresse",
                           "password": "Passwort"}

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, input):
        if len(input) > 2:
            self._email = input
        else:
            raise ValueError("Fehler")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, input):
        if len(input) > 12:
            self._password = input
        else:
            raise ValueError("min. 12 Zeichen")

    def to_dict(self):
        return {
            "email": self.email,
            "password": str(self.password)
        }

    def post_login_form(self):

        to_transmit = self.to_dict()

        url_part = "token"

        server_request = ServerRequest()

        success, self.response = server_request.make_post_request(url_part, to_transmit)

        return success
