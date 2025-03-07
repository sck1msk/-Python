def calculate_shipping_cost(item_count):
    if item_count <= 0:
        return 0.0
    

    first_item_cost = 10.95
    subsequent_item_cost = 2.95

    total_cost = first_item_cost +(item_count - 1) * subsequent_item_cost
    return total_cost

try:
    item_count = int(input("Введите количество товаров к покупке:"))
    if item_count < 0:
        print("количество товаров не может быть отрицательным")
    else: 
        total_cost = calculate_shipping_cost(item_count)
        print(f"общая стоимость доставки: ${total_cost:.2f}")
except ValueError:
    print("Введите корректное целое число")
