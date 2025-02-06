def count_characters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return sorted(counts.items(), key=lambda x: -x[1])

def assign_codes(symbols):
    if len(symbols) == 1:
        return {symbols[0][0]: ""}

    total = sum(freq for _, freq in symbols)
    split = next(i for i, (_) in enumerate(symbols) if sum(x[1] for x in symbols[:i + 1]) >= total / 2)
    left, right = symbols[:split + 1], symbols[split + 1:]
    codes = {}
    for symbol, code in assign_codes(left).items():
        codes[symbol] = "0" + code
    for symbol, code in assign_codes(right).items():
        codes[symbol] = "1" + code
    return codes

def encode_text(text):
    character_counts = count_characters(text)
    codes = assign_codes(character_counts)
    encoded = "".join(codes[char] for char in text)
    return encoded, codes

with open("tekst.txt", "r", encoding="utf-8") as file:
    input_text = file.read()

encoded_text, symbol_codes = encode_text(input_text)

with open("zadanie2_wynik.txt", "w", encoding="utf-8") as file:
    file.write(encoded_text)

print("The encoded text has been saved in 'encoded_text.txt'.")
print("\nCharacter codes:")
for symbol, code in symbol_codes.items():
    print(f"{repr(symbol)}: {code}")
