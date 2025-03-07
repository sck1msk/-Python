def check_even_odd(number):
    if number % 2 == 0:
        return "четное"
    else:
        return "нечетное"

# Запрос у пользователя целого числа
number = int(input("Введите целое число: "))

# Определение четности и вывод результата
result = check_even_odd(number)
print(f"Число {number} является {result}.")