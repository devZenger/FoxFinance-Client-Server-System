import os, sys, sqlite3

try:
    d = open("dax.csv")
except:
    print("Datei nicht geöffnet")
    sys.exit(0)

d.readline()
tx = d.read()
d.close()

li= tx.split("\n")

            
try:        
    connection = sqlite3.connect("../FoxFinanceData.db")
    print("Verbunden")
except:
    print("Fehler in der Verbundung")
    
cursor = connection.cursor()


sql = "SELECT index_id FROM stock_indexes WHERE name = 'DAX'"
cursor.execute(sql)

dax_id_tulp = cursor.fetchone()

dax_id = dax_id_tulp[0]

sql = f"SELECT name FROM stock_indexes WHERE index_id = {dax_id}"
cursor.execute(sql)

name_tulp = cursor.fetchone()

name = name_tulp[0]

if name == "DAX":
    print("korrekt")
else:
    print("Fehler index_id und name stimmen nicht")   
    

for zeile in li:
    if zeile:
        ds = zeile.split(",")
        sql = f"INSERT INTO stocks (isin, ticker_symbol, company_name) VALUES('{ds[0]}', '{ds[1]}', '{ds[2]}')"
        cursor.execute(sql)
        connection.commit()
        sql = f"INSERT INTO index_members (isin, index_id) VALUES('{ds[0]}', '{dax_id}')"
        cursor.execute(sql)
        connection.commit()
        
        print(f"{ds[0]} {ds[1]} {ds[2]}")
        

connection.close()