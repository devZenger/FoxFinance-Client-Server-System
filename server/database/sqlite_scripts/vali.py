import os, sys, sqlite3


path = os.path.join("..", "server", "database", "FoxFinanceData.db")

print(path)

if os.path.exists(path):
    print("Datenbank bereits vorhanden")

else:
    print("Datenbank nicht vorhanden")
    
connection = sqlite3.connect(path)
cursor = connection.cursor()

#customer related:

sql = """DROP TABLE validation"""

cursor.execute(sql)

connection.commit()


sql = """CREATE TABLE validation(
            customer_id INTEGER PRIMARY KEY REFERENCES customers(customer_id),
            validation_number INTEGER NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
            )"""
cursor.execute(sql)

sql = """CREATE TRIGGER update_date_trigger
            AFTER UPDATE OF validation_number ON validation
            FOR EACH ROW
            BEGIN
                UPDATE validation
                SET date = CURRENT_TIMESTAMP
                WHERE customer_id = NEW.customer_id;
        END"""

cursor.execute(sql)

connection.commit()



connection.close()