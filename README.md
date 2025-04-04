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
    customers ||--o{ stock_transactions : makes
    customers ||--o{ stock_watch_list : watch
    customers ||--o{ financial_transactions : makes
    customers {
        int customer_id PK
        string first_name "not null"
        string last_name "not null"
        string birthdate "not null"
        string email "not null"
        string phone_number "not null"
        string registration_date "not null"
        text termination_date
        text disabled
        string last_login "not null"
    }

    authentication ||--|| customers : use
    authentication {
        int customer_id PK, FK
        string password "not null"
    }

    customer_adresses ||--|| customers : owns
    customer_adresses{
        int customer_id PK, FK
        string street "not null"
        string house_number "not null"
        int zip_coide "not null"
        string city "not null"

    }

    financials ||--|| customers : has
    financials {
        int costumer_id PK, FK
        string reference_account "not null"
    }

    financial_transactions }o--|| financial_transactions_status : has
    financial_transactions{
        int financial_transaction_id PK
        int customer_id FK "not null"
        string bank_account "not null"
        decimal fin_amount "not null"
        string fin_transaction_type "not null"
        text usage 
        string fin_transaction_date "not null"
    }

    fin_transactions_types {
        int fin_transaction_type_id PK
        string fin_transaction_type "not null"
    }

    transactions ||--|| order_charges : contains
    transactions ||--o{ stocks : contains
    transactions {
        int transaction_id PK
        int customer_id FK "not null"
        string isin FK "not null"
        text transactions_type FK "not null"
        int amount "not null"
        decimal price_per_stock "not null"
        decimal order_charge_id "not null"
        string transaction_date "not null"
    }

    stocks ||--o{ stock_data : has
    stocks ||--o{ index_members : "is part"
    stocks {
        string isin PK 
        string ticker_symbol "not null"
        string company_name "not null"
    }
    stock_data {
        string dataID PK 
        string isin FK "not null"
        string date "not null"
        decimal open "not null"
        decimal close "not null"
        decimal high "not null"
        decimal low "not null"
        decimal close "not null"
        int volume "not null"
        decimal dividends "not null"
        decimal stock_splits "not null"
    }

    stock_watchlist ||--o{ stocks : contains
    stock_watchlist {
        int watchlist_id PK
        int customer_id FK "not null"
        string isin FK "not null"
        decimal price_per_stock "not null"
        string date "not null"
    }
        

    stock_indexes {
        int index_id PK "NOT NULL"
        string name "NOT NULL"
        string symbol "NOT NULL"
    }

    index_members }o--|| stock_indexes : includes
    index_members {
        string isin PK, FK "NOT NULL"
        int index_id PK, FK "NOT NULL"
    }

    order_charges {
    int order_charge_id PK
    string start_validation "not null"
    string end_validation "not null"
    decimal min_volumn "not null"
    decimal order_charge "not null"
    }

    validation {
        int customer_id PK, FK
        int validation_number "NOT NULL"
        text date "NOT NULL"
    }