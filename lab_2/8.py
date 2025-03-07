def isSublist(larger, smaller):
    if not smaller:
        return True  # Пустой список - подсписок любого списка
    
    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i+len(smaller)] == smaller:
            return True
    
    return False

# Тест
print(isSublist([1, 2, 3, 4], [2, 3]))  # True
print(isSublist([1, 2, 3, 4], [2, 4]))  # False
print(isSublist([1, 2, 3, 4], []))      # True
print(isSublist([1, 2, 3, 4], [1, 2, 3, 4]))  # True