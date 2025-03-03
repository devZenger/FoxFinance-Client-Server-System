import requests


formular_dic = {"last_name":"",
                "first_name": "",
                "street":"",
                "zip_code": "",
                "city": "",
                "birthday": "",
                "reference_account":"",
                "password":"",
                "email":"",
                "phone_number": "",
                "house_number": ""}

print("welcome to fox finance")

print("create new account")
formular_dic["last_name"] = input("Name eingaben: ")
formular_dic["first_name"] = input("Vorname eingeben: ")
formular_dic["street"] = input("Straße eingeben: ")
formular_dic["zip_code"] = input("Plz eingeben: ")
formular_dic["city"] = input("Stadt eingeben: ")
formular_dic["birthday"] = input("Geburtstag eingeben: ")
formular_dic["reference_account"] = input("Referenzekonto angeben: ")
formular_dic["password"] = input("Passwort eingeben: ")
formular_dic["phone_number"] = input("Telefonnummer: ")
formular_dic["email"] = input("email adresse: ")
formular_dic["house_number"] = input("hausnummer: ")



print("---------------------------------------------------------------------")

for data, v in formular_dic.items():
    print(f"{data} eingabe: {v}")


print("--------------------------------------------------------------------------")



url =  'http://127.0.0.1:8000/create_costumer_account/'

response = requests.post(url, json = formular_dic)

#back = response.json()
print(" ")
print(response.status_code)
print(" ")

if response.status_code == 200:
    print ("Empfangen:", response.json())
    #print(back)

else:
    print("Fehler", response.status_code)
    #print(back)
