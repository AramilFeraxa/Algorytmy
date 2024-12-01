class OdwrocWyrazy:
    def odwroc(self, tekst):
        wyrazy = tekst.split()
        odwracanie = wyrazy[::-1]
        return " ".join(odwracanie)

tekst = input("Podaj ciąg znaków: ")
odwroc_wyrazy = OdwrocWyrazy()
wynik = odwroc_wyrazy.odwroc(tekst)
print(f"Wynik: {wynik}")