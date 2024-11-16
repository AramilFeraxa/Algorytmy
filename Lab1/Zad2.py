def MinAndMax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    return min, max

print("Podaj liczby: ")
arr = [int(x) for x in input().split()]
print("Najmniejsza liczba to: ", MinAndMax(arr)[0])
print("Najwieksza liczba to: ", MinAndMax(arr)[1])