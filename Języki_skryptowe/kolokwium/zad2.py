import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def oblicz_odleglosc(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Błędne dane. Proszę podać liczbę.")

x1 = get_float_input("Podaj współrzędną x dla punktu 1: ")
y1 = get_float_input("Podaj współrzędną y dla punktu 1: ")
punkt1 = Punkt(x1, y1)

x2 = get_float_input("Podaj współrzędną x dla punktu 2: ")
y2 = get_float_input("Podaj współrzędną y dla punktu 2: ")
punkt2 = Punkt(x2, y2)

odleglosc = oblicz_odleglosc(punkt1, punkt2)
print(f"Odległość między punktami wynosi: {odleglosc:.2f}")