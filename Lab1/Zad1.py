def Max(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

print("Podaj liczby: ")
arr = [int(x) for x in input().split()]
print("Największa liczba to: ", Max(arr))