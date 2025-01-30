class Auto:
    def __init__(self, znacka, barva):
        # Atributy třídy
        self.znacka = znacka  # Atribut 'znacka'
        self.barva = barva    # Atribut 'barva'

    def popis(self):
        # Metoda třídy
        return f"Toto auto je {self.barva} {self.znacka}."

def vytvor_auto(znacka, barva):
    # Funkce, která vytváří instanci třídy Auto
    return Auto(znacka, barva)

# Vytvoření instance třídy Auto
moje_auto = vytvor_auto("Škoda", "modrá")

# Výpis popisu auta
print(moje_auto.popis())