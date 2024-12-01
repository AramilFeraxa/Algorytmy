def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                new_char = chr((ord(char) - start + shift) % 26 + start)
            elif mode == "decrypt":
                new_char = chr((ord(char) - start - shift + 26) % 26 + start)
            result += new_char
        else:
            result += char
    
    return result

def main():
    print("Szyfr Cezara")
    print("Wybierz opcję:")
    print("1. Szyfrowanie")
    print("2. Deszyfrowanie")
    
    try:
        choice = int(input("Wpisz numer opcji (1/2): "))
        if choice not in [1, 2]:
            raise ValueError("Nieprawidłowa opcja. Wybierz 1 lub 2.")
        
        text = input("Podaj tekst: ")
        shift = int(input("Podaj przesunięcie (liczba całkowita): "))
        
        if choice == 1:
            mode = "encrypt"
        else:
            mode = "decrypt"
        
        result = caesar_cipher(text, shift, mode)
        print(f"Wynik: {result}")
    
    except ValueError as e:
        print(f"Błąd: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

main()