# Projekt: FoxFinance - A Server-Client Projekt
FoxFinance ist ein Server-Client-Projekt, das es Nutzern ermöglicht, ein Aktiendepot zu eröffnen und Aktien zu handeln.
Das Client-Programm dient als Benutzerschnittstelle, während das Server_Programm die Verwaltung von Konten und Transaktionen übernimmt. Die Daten werden in einer SQLite-Datenbank gespeichert.
- Das Client-Programm  ist eine Konsolenanwendung, umgesetzt nach dem **MVC-Pattern**.
- Das Server-Programm basiert auf einer **mehrschichtigen Architektur** (Schichenarchitektur)
- Implementiert wurde das Projekt in **Python** unter Einsatz von **FastAPI** und **SQLite**.

Hinweis:  
Für Geldbeträge wird `float` statt `Deciaml` verwendet, da SQLite3 `Decimal` nicht unterstützt. Da die Genauigkeit nicht im Vordergrund stand, wurde für Geldbeträge `float` und in der Datenbank `REAL` genutzt.

<div style="text-align: center;">
<b>Customer-Client Programm: Startmenü</b> <br>
<img src="docs/images/Screenshot_Startmenu.png" alt="Startmenü" title="Customer-Client Programm Startmenu" style="width:80%; height:auto;">
</div>


## Inhaltsverzeichnis:
- [Vewendete Technologien](#verwendete-technologien)
- [Projektvorstellung](#projektvorstellung)
- [Projektübersicht](#projektübersicht)
  - [Funktionen](#funktionen)
  - [Projektverzeichnis](#projectverzeichnis)
  - [Uml Klassendiagramm](#uml-klassendiaggramm)
  - [Relationale Datenbankdiagramm](#relationales-datenbankmodell)
- [Screenshoots](#screenshots)
- [Lizenz](#lizenz)

## Verwendete Technologien:
- Programmiersprachen:
  - Python
  - SQL ?
- Frameworks & Tools:
  - FastAPi – REST-API Framework
  - SQLite – OpenSource Datenbank  
  - YFinance – zum einlesen Aktiendaten
  - UVicorn – ASGI-Server für FastAPI
- weitere Bibliotheken:
  - ``os``, ``sys`` – Systemfunktionen
  - ``request`` – HTTP-Anfragen
  - ``datetime`` – Zeitverarbeitung
  - ``getpass`` – Passwort-Eingabe ohne Anzeige
  - ``jwt``, ``passlib.context`` – Authentifizierung & Passwort-Hashing
  - ``pydantic`` – Datenvalidierung
  - ``typing`` – Typannotationen
- Diagrammtools:
  - PlantUML – Klassendiagrammen
  - dbdiagram.io – relationalen Datenbankmodell


## Projektvorstellung:
Der Hintergrund des Projekts war es, ein tieferes Verständnis von **Python**, **SQL** und den Aufbau von **REST-APIs** zu entwickeln. Aus persönlichen Interesse entschied ich mich für das Thema **Aktendepots und Aktienhandel**, da es sich um ein spannendes Thema handelt und sich gut f+ür die Umsetzung eines vollständigen Server-Client-Systems eignet.  
Die Wahl fiel auf **SQLite** als Datenbank, da es sich nathlos in Python integrieren lässt und es praktische Erweiterung für die Entwicklungsumgebungen Visual Studio Code gibt.  
Das Projekt besteht aus vier Teile, die Client-Anwendung, das Server-Programm, die Kommunikation über eine **REST-API** und die SQLite Datenbank

Die Client-Anwendung ist ein Konsolenprogramm im **MVC-Pattern** geschrieben, dadurch ist das Programm klar unterteilt was die **Wartbarkeit und Testbarkeit** erhöht. Es wurde eine grundlegende **Fehlerbehandlung** integriert, um ungüligte Benutzereingaben abzufangen. getter setter erwähnen?
Bei der Erstellung des Konto wurde darauf geachtet das das Passwort sicher ist Standard erwähnen? 2 Faktor für Konot freischaltung erwähnen?  
Wo es sich anbot wurde mit Klassen und Vererbung gearbeitet, um gemeinsame Logik zentral bereitzustellen und eine Trennung von Zuständigkeiten umzusetzten. 
Desweiteren wurde nach dem DRY-Prinzip gearbeitet und Service-Klassen erstellt und Funktionen in utilit.py geschrieben um Wiederholungen vom Programmcode zu vermeiden. Das Auslesen und Setzen von Eigenschaften wird mit Hilfe von Reflection dynamisch umgesetzt.

Das Serverprogramm ist in einer SChichtenarchitektur umgesetzt. Die Hauptschichten sind api, service und repository. Auf SQLAlchemy wurde bewusst verzichtet um SQL-Befehle zu benutzen. Für die Fehlermeldung wurde ein eigener Logger geschrieben.

Die relationale Datenbank ist in verschiedene Tabellen aufgeteilt. Um den Datenschutz gerecht zu werden, wurden die Daten der Kunden aufgeteilt in Adresse, Authentivation, Finanzen und Allgemein. Außerdem werden das Passwort und die Kontonummer verschlüsselt.

Die REST-Api wurde mit FAST-API umgesetzt bla bla . Die Client-Anwendung sendet seine Anfrage mit Hilfe der `request`Bibliothek


Ursrpünglich war die Absicht, ein zweites Client-Programm zu erstellen, um auch die Bankseite zu repräsentieren. Dies wurde aus Zeitgründen um das Projekt abzuschließen, verworfen. 

 

## Projektübersicht

### Funktionen:
- Start des Servers
- Erstellen ein Kontos
- Login in das Konto
- Funktionen des Depot
  - Aktien suchen
  - Aktien handeln
  - Watchlist erstellen
  - Kontoübersicht
  - Geld ein-/auszahlen
  - Informationen (Ordergebühren)
  - Daten ändern
  - Abmelden
  - Abmelden und beenden
- Informationen (Ordergebühren)
- Beenden

### Projectverzeichnis
Ein komplettes Verzeichnis findet sich hier: Link

<pre style="font-size:10px; font-family:Consolas;">
FoxFinance/
├── customer_client/
│    ├── controller/
│    ├── model/
│    ├── service/
│    ├── view/
│    └── app.py
├── docs/
│    └── images/
├── server/
│    ├── api/
│    ├── database/
│    │    ├── sqlite_scripts/
│    │    └── FoxFinanceData.db
│    ├── logger/
│    ├── repository/
│    ├── schemas/
│    ├── service/
│    └── main_server.py
└── README.md
</pre>

### UML Klassendiaggramm
[wird noch eingefügt]
### Relationales Datenbankmodell
[wird noch eingefügt]
## Screenshots
[wird noch eingefügt]

## Lizenz
Dieses Projekt wurde ausschließlich zu **Lern- und Demonstrationszwecken** entwickelt.  
Die Nutzung des Quellcodes ist for den privaten, nicht-kommerziellen Gebrauch gestattet   

Eine Weitergabe, Veränderung oder kommerzielle Nutzung ist nur mit ausdrücklicher Genehmigung erlaubt.  

Bei Fragen oder Feedback freue ich mich über eine Nachricht.