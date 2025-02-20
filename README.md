Projektziel:
Ein besseres Verständnis von Python und SQL durch die Entwicklung eines Programms zur Veraltung von Aktiendepots.
Besonderes Augenmerkt auf Klassen und Vererbung

Ideen:
````mermaid
mindmap
    root((Aktiendepot<br>Verwaltung))
        Hauptmenü
            Testdepot
            Neues Konto erstellen
            Kundenlogin
                Kundenmenü
                    Depot Übersicht
                    Aktien kauf/verkauf
                    Kursübersicht
                    Postfach
            Informationen
            Programm beenden
            
        Kunden Verwaltung
            Kundenanfragen
            Kundenübersicht
            Aktienübersicht
````


````mermaid
erDiagram
    customers ||--o{ transactions : makes
    customers ||--o{ stock_watch_list : watch
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

    financials ||--|| customers : has
    financials {
        int costumer_id PK, FK
        string reference_account "not null"
        decimal balance "not null"
    }

    transactions ||--o{ stocks : contains
    transactions {
        int transaction_id PK
        int customer_id FK "not null"
        string wkn FK "not null"
        enum action "not null"
        int count "not null"
        decimal price_per_stock "not null"
        decimal order_charge "not null"
        string transaction_date "not null"
    }

    stocks ||--o{ stock_data : has
    stocks ||--o{ index_members : "is part"
    stocks {
        string wkn PK 
        string ticker_symbol "not null"
        string company_name "not null"
    }
    stock_data {
        string dataID PK 
        string wkn FK "not null"
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
    employees {
        int emplayee_id PK
        string name "not null"
        string email_adress "not null"
        string password "not null"
    }

    stock_watch_list ||--o{ stocks : contains
    stock_watch_list {
        int watchlist_id PK
        int customer_id FK "not null"
        string wkn FK "not null"
        decimal price_per_stock "not null"
        string transaction_date "not null"
    }
        

    stock_indexes {
        int index_id PK "NOT NULL"
        string name "NOT NULL"
        string symbol "NOT NULL"
    }

    index_members ||--|| stock_indexes : includes
    index_members {
        string wkn PK, FK "NOT NULL"
        int index_id PK, FK "NOT NULL"
    }
