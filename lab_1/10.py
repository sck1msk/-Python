import math

def arithmetic_operations():

    a = int(input("Введите первое целое число (a): "))
    b = int(input("Введите второе целое число (b): "))

    print(f"Сумма a и b: {a + b}")
    print(f"Разность между a и b: {a - b}")
    print(f"Произведение a и b: {a * b}")
    if b != 0:
        print(f"Частное от деления a на b: {a / b:.2f}")
        print(f"Остаток от деления a на b: {a % b}")
    else:
        print("Деление на ноль невозможно.")

    if a > 0:
        print(f"Десятичный логарифм числа a: {math.log10(a):.2f}")
    else:
        print("Логарифм от неположительного числа невозможно вычислить.")

    print(f"Результат возведения числа a в степень b: {a ** b}")

if __name__ == "__main__":
    arithmetic_operations()
