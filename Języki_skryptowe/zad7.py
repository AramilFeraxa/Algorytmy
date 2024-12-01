import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def oblicz_odleglosc(p1, p2):
    """Oblicza odległość między dwoma punktami."""
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

x1 = float(input("Podaj współrzędną x dla punktu 1: "))
y1 = float(input("Podaj współrzędną y dla punktu 1: "))
punkt1 = Punkt(x1, y1)
        
x2 = float(input("Podaj współrzędną x dla punktu 2: "))
y2 = float(input("Podaj współrzędną y dla punktu 2: "))
punkt2 = Punkt(x2, y2)
        
odleglosc = oblicz_odleglosc(punkt1, punkt2)
print(f"Odległość między punktami wynosi: {odleglosc:.2f}")