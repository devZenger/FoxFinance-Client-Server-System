import requests


# just to try out the server

url = 'http://127.0.0.1:8000/information/'

response = requests.get(url)

if response.status_code == 200:
    print ("Empfangen:", response.json())

else:
    print("Fehler", response.status_code)
