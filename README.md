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
            Firmenportal
            Programm beenden
            
        Kunden Verwaltung
            Kundenanfragen
            Kundenübersicht
            Aktienübersicht
````


````mermaid
erDiagram
    customers ||--o{ transactions : makes
    customers ||--o{ stock_watch : has
    customers {
        int customer_id PK "not null"
        string name "not null"
        string email "not null"
        string phone_number "not null"
        string birthdate "not null"
        decimal deposit
        string reference_account "not null"
        string password "not null"
        string registration_date "not null"
    }
    transactions ||--o{ stocks : contains
    transactions {
        int transaction_id PK "not null"
        int customer_id FK "not null"
        string wkn FK "not null"
        enum action "not null"
        int count "not null"
        decimal price_per_stock "not null"
        decimal order_charge "not null"
        string transaction_date "not null"
        }

    stocks ||--o{ stock_data : has
    stocks {
        string wkn PK "not null"
        string ticker_symbol "not null"
        string company_name "not null"
    }
    stock_data {
        string dataID PK "not null"
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
        int emplayee_id PK "not null"
        string name "not null"
        string email_adress "not null"
        string password "not null"
    }

    stock_watch ||--o{ stocks : contains
    stock_watch {
        int watchlist_id PK "not null"
        int customer_id FK "not null"
        string wkn FK "not null"
        decimal price_per_stock "not null"
        string transaction_date "not null"
    }
        
        

