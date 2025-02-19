class LoginForm:
    def __init__(self):
        self._email = None
        self._password = None
    
    
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
        return self.password
    @password.setter
    def password(self, input):
        if len(input) > 12:
            self.password = input
        else:
            raise ValueError("Fehler")
    
    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password
        }
    