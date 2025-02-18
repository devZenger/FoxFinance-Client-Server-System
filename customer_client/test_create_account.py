import requests


formular_dic = {"lastname":"", "firstname": "", "street":"", "zip_code": 0, "city": "", "birthday": "", "reference_account":"", "password":"", "email":"", "phone": 0}

print("welcome to fox finance")
print("create new account")
formular_dic["lastname"] = input("Name eingaben: ")
formular_dic["firstname"] = input("Vorname eingeben: ")
formular_dic["street"] = input("Straße eingeben: ")
formular_dic["zip_code"] = input("Plz eingeben: ")
formular_dic["city"] = input("Stadt eingeben: ")
formular_dic["birthday"] = input("Geburtstag eingeben: ")
formular_dic["reference_account"] = input("Referenzekonto angeben: ")
formular_dic["password"] = input("Passwort eingeben: ")
formular_dic["phone"] = input("Telefonnummer: ")
formular_dic["email"] = input("email adresse: ")


url =  'http://127.0.0.1:5000/create_customer_account/'

response = requests.post(url, json = formular_dic)

if response.status_code == 200:
    print ("Empfangen:", response.json())

else:
    print("Fehler", response.status_code)

