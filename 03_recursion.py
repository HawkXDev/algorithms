def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(f'{fact(7) = }')


def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


print(f'{sum([4,2,8,6]) = }')


def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


print(f'{count([1,2,3,4,5,6,7,8,9,10]) = }')


def max(list):
    if len(list) == 1:
        return list[0]
    else:
        sub_max = max(list[1:])
        return list[0] if list[0] > sub_max else sub_max


print(f'{max([3,7,2,9,11,4]) = }')


def binary_search(list, item):
    if len(list) == 1:
        return True if list[0] == item else False
    else:
        mid = int(len(list) / 2)
        return binary_search(list[:mid], item) or binary_search(list[mid:], item)


print(f'{binary_search([3,4,7,10,13,17,20], 7) = }')
