import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return arr[mid]

def partition_with_median(arr, low, high):
    pivot = median_of_three(arr, low, high)
    pivot_index = high
    for i in range(low, high + 1):
        if arr[i] == pivot:
            pivot_index = i
            break
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def quicksort_with_median(arr, low, high):
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition_with_median(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def measure_sorting_time():
    size = 1_000_000
    data = [random.randint(0, 10_000) for _ in range(size)]

    data_copy = data[:]

    start = time.time()
    quicksort(data, 0, len(data) - 1)
    end = time.time()
    standard_time = end - start
    print(f"Standard quicksort time: {standard_time:.4f} seconds")

    start = time.time()
    quicksort_with_median(data_copy, 0, len(data_copy) - 1)
    end = time.time()
    median_time = end - start
    print(f"Quicksort with median of three time: {median_time:.4f} seconds")

    print(f"{'Standard' if standard_time < median_time else 'Median of three'} is faster")

if __name__ == "__main__":
    measure_sorting_time()
