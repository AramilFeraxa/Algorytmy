def isPalindrome(a):
    if a == a[::-1]:
        return "Wyraz " + a + " jest palindromem"
    else:
        return "Wyraz " + a + " nie jest palindromem"

print(isPalindrome("kajak"))
print(isPalindrome("kurtka"))