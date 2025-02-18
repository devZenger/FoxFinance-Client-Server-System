from forms import RegistrationForm



    
def display_form(form):
    for key in form:
        try :
            form[key] = input(f"{key} eingeben: ")
        except Exception as e:
            print("Fehlerhafte eingabe: {e}")
            form[key] = input(f"{key} eingeben: ")

    # Fügt hier die Fehlermeldung hinzu, wenn ein Wert leer ist
    for key, item in form.items():  # items()-Methode verwenden, um Schlüssel und Werte zu iterieren
        if len(item) > 0:
            print(f"{key} {item}")

def main():
    test = RegistrationForm()
    testdic = {
        "Familiennamen": test.last_name,
        "Vornamen": test.first_name,
        "Straße": test.street,
        "Hausnummer": test.house_number,
        "PLZ": test.zip_code,
        "Wohnort": test.city,
        "Geburtstag": test.birthday,
        "E-Mail Adresse":test.email,
        "Handynummer": test.phone_number,
        "Referenzkonto (IBAN)": test.reference_acccount,
        "Passwort": test.password
    }

    display_form(testdic)

if __name__ == "__main__":
    main()

       # for key, item in form:
        #    if len(item) > 0:
         
         #       print("test") 
           
          #      print(f"{key}: {item}")





                