def isPalindrome(s):
    return s == s[::-1]

text = input("Podaj tekst: ")
if isPalindrome(text):
    print("Tekst jest palindromem.")
else:
    print("Tekst nie jest palindromem.")