import matplotlib.pyplot as plt

# Beispiel-Daten
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Erstelle das Diagramm
plt.plot(x, y)

# Füge Titel und Achsenbeschriftungen hinzu
plt.title('Einfaches Diagramm')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')

# Zeige das Diagramm an
plt.show()