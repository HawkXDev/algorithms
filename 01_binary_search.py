def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


mylist = [1, 3, 5, 7, 9]

print(f'{mylist = }')
print(f'{binary_search(mylist, 9) = }')
print(f'{binary_search(mylist, -1) = }')
