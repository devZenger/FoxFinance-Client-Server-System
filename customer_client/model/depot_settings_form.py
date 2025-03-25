from .registration_form import RegistrationForm
from .server_request_depot import ServerRequestDepot

class SettingsForm(RegistrationForm):
    def __init__(self, token):
        self.token = token
        
        
        #self._last_name = None
        #self._street = None
        #self._house_number = None
        #self._zip_code = None
        #self._city = None
        #self._email = None
        #self._phone_number = None
        #self._reference_account = None
        #self._password = None
        
        
        self.form_names_adress = {
            "street": "Straße (ohne Hausnummer)",
            "house_number": "Hausnummer",
            "city": "Stadt",
            "zip_code": "Postleitzahl",
        }

        self.form_names_phone_number = {
            "email" : "E-Mail Adresse",
            "reference_account": "Referenzkonto",
            "password": "Passwort"
        }

        self.form_names_email_adress = {
            "email" : "E-Mail Adresse",
        }

        self.form_names_reference_account = {
            "reference_account": "Referenzkonto",
        }

        self.form_names_password = {
            "password": "Passwort"
        }
  

        super().__init__()
              
                
        self.name_settings = self.form_names
        del self.name_settings["fin_amount"] 

    def transmit_changes(self, type:str):
        
        to_transmit = {}
        
        match type:
            
            case "adress":
                to_transmit = {"transmission_type":"adress",
                               "street": self.street,
                               "house_number": self.house_number,
                               "city": self.city,
                               "zip_code": self.zip_code,}
                
            case "phone_number":
                to_transmit = {"transmission_type":"phone_number",
                               "phone_number":self.phone_number}
            case "email":
                to_transmit = {"transmission_type":"email",
                               "phone_number":self.email}
            case "reference_account":
                to_transmit = {"transmission_type":"reference_account",
                               "phone_number":self.reference_acccount}
            case "password":
                to_transmit = {"transmission_type":"password",
                               "phone_number":self.password}
            case _:
                return print("fehler")
            
        server_request = ServerRequestDepot(self.token)
        
        url_part = "changesettings/"
        
        print(f"to transmit is {to_transmit}")
        
        response = server_request.make_post_request(url_part, to_transmit)
        
        del server_request
        
        if response == "Updated":
            return "start"
        else:
            self.error = response
            return "error"
            
        
        return response
    
    def current_settings(self):
        
        server_request = ServerRequestDepot(self.token)
        
        url_part = "settings/"
        
        response = server_request.get_with_parameters(url_part)
        
        del server_request
        
        return response
        
          
          
            
            
        