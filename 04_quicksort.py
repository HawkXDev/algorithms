def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = quicksort([x for x in arr[1:] if x < arr[0]])
        greater = quicksort([x for x in arr[1:] if x >= arr[0]])
        return less + [pivot] + greater


arr = [3, 8, 4, 10, 0, 7, 5]
print(f'{arr = }')
print(f'{quicksort(arr) = }')
