def suma(*args):
    # Założyłem, żeby nie używać funkcji wbudowanej sum()
    total = 0
    for arg in args:
        total += arg
    return total

def mediana(*args):
    args = sorted(args)
    n = len(args)
    if n % 2 == 0:
        return (args[n//2 - 1] + args[n//2]) / 2
    else:
        return args[n//2]
    
def avg(*args):
    return suma(*args) / len(args)

print("Wybierz operację:")
print("1. Suma")
print("2. Mediana")
print("3. Średnia")

try:
    choice = int(input("Wpisz numer operacji (1/2/3): "))
    if choice not in [1, 2, 3]:
        raise ValueError("Nieprawidłowy wybór operacji.")
    
    numbers = [float(x) for x in input("Podaj liczby (oddzielone spacją): ").split()]
    
    if choice == 1:
        print(f"Suma: {sum(*numbers)}")
    elif choice == 2:
        print(f"Mediana: {mediana(*numbers)}")
    elif choice == 3:
        print(f"Średnia: {avg(*numbers)}")
except ValueError as e:
    print(f"Błąd: {e}")
except Exception as e:
    print(f"Nieoczekiwany błąd: {e}")