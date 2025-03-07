def main():
    # Запрашиваем у пользователя количество сувениров и безделушек
    num_souvenirs = int(input("Введите количество сувениров: "))
    num_trinkets = int(input("Введите количество безделушек: "))

    # Вес каждого товара
    weight_souvenir = 75  # вес сувенира в граммах
    weight_trinket = 112  # вес безделушки в граммах

    # Расчет общего веса посылки
    total_weight = (num_souvenirs * weight_souvenir) + (num_trinkets * weight_trinket)

    # Вывод общего веса
    print(f"Общий вес посылки: {total_weight} грамм(ов)")

if __name__ == "__main__":
    main()
