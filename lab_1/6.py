def main():
    # Запрашиваем у пользователя сумму заказа
    order_amount = float(input("Введите сумму заказа в ресторане: "))

    # Определяем налоговую ставку и расчет налога
    tax_rate = 0.10  # Здесь указана налоговая ставка в 10%
    tax = order_amount * tax_rate

    # Расчет чаевых (18% от суммы заказа без учета налога)
    tip_rate = 0.18
    tip = order_amount * tip_rate

    # Расчет итоговой суммы
    total = order_amount + tax + tip

    # Вывод результатов с форматированием
    print(f"Налог: ${tax:.2f}")
    print(f"Чаевые: ${tip:.2f}")
    print(f"Итоговая сумма: ${total:.2f}")

if __name__ == "__main__":
    main()
