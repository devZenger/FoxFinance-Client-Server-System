import os, sys, sqlite3


path = os.path.join("FoxFinanceData.db")

print(path)

if os.path.exists(path):
    print("Datenbank bereits vorhanden")
    sys.exit(0)
else:
    print("Datenbank nicht vorhanden")
    
connection = sqlite3.connect(path)
cursor = connection.cursor()