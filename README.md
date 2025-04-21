Projektziel:
Ein besseres Verständnis von Python und SQL durch die Entwicklung eines Programms zur Veraltung von Aktiendepots.
Besonderes Augenmerkt auf Klassen und Vererbung

Ideen:
````mermaid
mindmap
    root((Aktiendepot<br>Verwaltung))
        Willkomensmenü
            Testdepot
            Neues Konto erstellen
            Kundenlogin
                Kundenmenü
                    Depot Übersicht
                        Liste an Aktien
                        Gewinn/Verlust
                    Aktien kauf/verkauf
                    Kursübersicht
                    Kontotransaktionen
                    Änderungen der Daten
            Informationen
            Programm beenden
            
   
````


````mermaid
erDiagram
    customers ||--o{ transactions : makes
    customers ||--o{ stock_watchlist : watch
    customers ||--o{ financial_transactions : makes
    customers {
        int customer_id PK
        text first_name "not null"
        text last_name "not null"
        text birthdate "not null"
        text email "not null"
        text phone_number "not null"
        text registration_date "not null"
        text termination_date
        text disabled
        text last_login "not null"
    }

    authentication ||--|| customers : use
    authentication {
        int customer_id PK, FK
        text password "not null"
    }

    customer_adresses ||--|| customers : owns
    customer_adresses{
        int customer_id PK, FK
        text street "not null"
        text house_number "not null"
        int zip_coide "not null"
        text city "not null"

    }

    financials ||--|| customers : has
    financials {
        int costumer_id PK, FK
        text reference_account "not null"
    }

    financial_transactions }o--|| fin_transactions_types : has
    financial_transactions{
        int financial_transaction_id PK
        int customer_id FK "not null"
        text bank_account "not null"
        float fin_amount "not null"
        text fin_transaction_type "not null"
        text usage 
        text fin_transaction_date "not null"
    }

    fin_transactions_types {
        int fin_transaction_type_id PK
        text fin_transaction_type "not null"
    }

    transactions ||--|| order_charges : contains
    transactions ||--o{ stocks : contains
    transactions {
        int transaction_id PK
        int customer_id FK "not null"
        text isin FK "not null"
        text transactions_type FK "not null"
        int amount "not null"
        float price_per_stock "not null"
        float order_charge_id "not null"
        text transaction_date "not null"
    }

    stocks ||--o{ stock_data : has
    stocks ||--o{ index_members : "is part"
    stocks {
        text isin PK 
        text ticker_symbol "not null"
        text company_name "not null"
    }
    stock_data {
        text dataID PK 
        text isin FK "not null"
        text date "not null"
        float open "not null"
        float close "not null"
        float high "not null"
        float low "not null"
        float close "not null"
        int volume "not null"
        float dividends "not null"
        float stock_splits "not null"
    }

    stock_watchlist ||--o{ stocks : contains
    stock_watchlist {
        int watchlist_id PK
        int customer_id FK "not null"
        text isin FK "not null"
        float price_per_stock "not null"
        text date "not null"
    }
        

    stock_indexes {
        int index_id PK "NOT NULL"
        text name "NOT NULL"
        text symbol "NOT NULL"
    }

    index_members }o--|| stock_indexes : includes
    index_members {
        text isin PK, FK "NOT NULL"
        int index_id PK, FK "NOT NULL"
    }

    order_charges {
    int order_charge_id PK
    text start_validation "not null"
    text end_validation "not null"
    float min_volumn "not null"
    float order_charge "not null"
    }

    validation {
        int customer_id PK, FK
        int validation_number "NOT NULL"
        text date "NOT NULL"
    }