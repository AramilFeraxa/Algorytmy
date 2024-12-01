def quick_sort(arr):
    def sort_helper(arr, low, high):
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        if low < high:
            pi = partition(arr, low, high)
            sort_helper(arr, low, pi - 1)
            sort_helper(arr, pi + 1, high)

    sort_helper(arr, 0, len(arr) - 1)

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(arr))