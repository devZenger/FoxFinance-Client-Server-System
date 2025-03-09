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
    customers ||--o{ balance_transactions : makes
    customers {
        int customer_id PK
        string registration_date "not null"
        string last_login "not null"
    }

    authentication ||--|| customers : use
    authentication {
        int customer_id PK, FK
        string email "not null"
        string phone_number "not null"
        string password "not null"
    }

    customer_adresses ||--|| customers : owns
    customer_adresses{
        int customer_id PK, FK
        string first_name "not null"
        string last_name "not null"
        string street "not null"
        string house_number "not null"
        int zip_coide "not null"
        string city "not null"
        string birthdate "not null"
    }

    zip_codes ||--o{ customer_adresses : has
    zip_codes {
        int zip_code PK
        string city
    }

    financials ||--|| customers : has
    financials {
        int costumer_id PK, FK
        string reference_account "not null"
    }

    balance_transactions }o--|| balance_transactions_status : has
    balance_transactions{
        int balance_transaction_id PK
        int customer_id FK "not null"
        string bank_account "not null"
        decimal balance_sum "not null"
        string kind_of_action "not null"
        string transaction_date "not null"
    }

    balance_transactions_status {
        int balance_transaction_status_id PK
        string type_of_action "not null"
    }

    stock_transactions ||--|| order_charges : contains
    stock_transactions ||--o{ stocks : contains
    stock_transactions {
        int stock_transaction_id PK
        int customer_id FK "not null"
        string isin FK "not null"
        int transactions_status_id FK "not null"
        int count "not null"
        decimal price_per_stock "not null"
        decimal order_charge "not null"
        string transaction_date "not null"
    }

    transaction_status ||--o{ stock_transactions : has
    transaction_status{
        int transactions_status_id PK
        string kind_of_action "not null"
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

    stock_watch_list ||--o{ stocks : contains
    stock_watch_list {
        int watchlist_id PK
        int customer_id FK "not null"
        string isin FK "not null"
        decimal price_per_stock "not null"
        string transaction_date "not null"
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
    decimal min_stock_vol "not null"
    decimal order_charge_base "not null"
    decimal order_charge_provision "not null"
}
