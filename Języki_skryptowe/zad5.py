import os

def count_spaces_in_file(input_file, output_file):
    try:        
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            space_count = 0
            for char in content:
                if char == ' ':
                    space_count += 1
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"Liczba spacji w pliku '{input_file}': {space_count}")
        
        print(f"Zliczanie zakończone. Wynik zapisano w pliku '{output_file}'.")
    
    except FileNotFoundError as e:
        print(f"Błąd: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

input_file = "text.txt"
output_file = "wynik.txt"
    
count_spaces_in_file(input_file, output_file)