

class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def beschleunigung(self, wert):
        self.geschwindigkeit +=wert
        print(self.geschwindigkeit)
        
        
class PKW(Fahrzeug):
    def __init__(self, bez, ge, ins):
        super().__init__(bez, ge)
        self.insassen = ins
    def run(self):
        self.geschwindigkeit(40)