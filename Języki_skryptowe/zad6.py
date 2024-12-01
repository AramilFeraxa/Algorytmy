import math

class Kolo:
    def __init__(self, promien):
        if promien <= 0:
            raise ValueError("Promień musi być liczbą dodatnią.")
        self.promien = promien

    def oblicz_pole(self):
        """Oblicza pole koła."""
        return math.pi * self.promien ** 2

    def oblicz_obwod(self):
        """Oblicza obwód koła."""
        return 2 * math.pi * self.promien


promien = float(input("Podaj promień koła: "))
kolo = Kolo(promien)
print(f"Pole koła: {kolo.oblicz_pole():.2f}")
print(f"Obwód koła: {kolo.oblicz_obwod():.2f}")