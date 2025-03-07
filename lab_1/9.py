def calculate_compound_interest():
    # Запрашиваем сумму первоначального депозита у пользователя
    initial_deposit = float(input("Введите сумму первоначального депозита: "))
    interest_rate = 0.04  # Процентная ставка: 4% годовых

    # Рассчитываем сумму на конец каждого года
    year1 = initial_deposit * (1 + interest_rate)
    year2 = year1 * (1 + interest_rate)
    year3 = year2 * (1 + interest_rate)

    # Выводим результаты с округлением до двух знаков
    print(f"Сумма на счету в конце первого года: {year1:.2f}")
    print(f"Сумма на счету в конце второго года: {year2:.2f}")
    print(f"Сумма на счету в конце третьего года: {year3:.2f}")

if __name__ == "__main__":
    calculate_compound_interest()
