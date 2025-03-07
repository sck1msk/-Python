def calculate_change(cents):
    coins = {200: "2 CAD", 100: "1 CAD", 25: "25 cents", 10: "10 cents", 5: "5 cents", 1: "1 cent"}
    change = {}
    
    for value, name in coins.items():
        if cents >= value:
            count = cents // value
            cents %= value
            change[name] = count
    
    return change

# Запрос у пользователя суммы сдачи в центах
cents = int(input("Введите сумму сдачи в центах: "))

if cents < 0:
    print("Сумма не может быть отрицательной.")
else:
    change = calculate_change(cents)
    print("Необходимо выдать:")
    for coin, count in change.items():
        print(f"{count} x {coin}")
