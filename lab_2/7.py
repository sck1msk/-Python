def center_string(s, w):

    if len(s) >= w:
        return s
    padding = (w - len(s)) // 2
    return ' ' * padding + s

print("\nЦентрируем строки:")
test_strings = ["Пример", "Центрирование", "Python"]
widths = [20, 30, 15]

for s, w in zip(test_strings, widths):
    print(f"'{center_string(s, w)}'")
