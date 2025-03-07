def isSorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

# Тест
print(isSorted([1, 2, 3, 4]))  # True
print(isSorted([4, 3, 2, 1]))  # True
print(isSorted([1, 3, 2, 4]))  # False
print(isSorted([5]))           # True
print(isSorted([]))            # True