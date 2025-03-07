def allSublists(lst):
    sublists = [[]]  # Всегда включаем пустой список
    
    for start in range(len(lst)):
        for end in range(start + 1, len(lst) + 1):
            sublists.append(lst[start:end])
    
    return sublists

# Тест
print(allSublists([1, 2, 3]))  # [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]