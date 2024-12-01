def calculator():
    print("Kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    
    try:
        choice = int(input("Wpisz numer operacji (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError("Nieprawidłowy wybór operacji.")
        
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        
        if choice == 1:
            print(f"Wynik: {num1} + {num2} = {num1 + num2}")
        elif choice == 2:
            print(f"Wynik: {num1} - {num2} = {num1 - num2}")
        elif choice == 3:
            print(f"Wynik: {num1} * {num2} = {num1 * num2}")
        elif choice == 4:
            if num2 == 0:
                print("Błąd: Dzielenie przez zero jest niedozwolone.")
            else:
                print(f"Wynik: {num1} / {num2} = {num1 / num2}")
    except ValueError as e:
        print(f"Błąd: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

calculator()