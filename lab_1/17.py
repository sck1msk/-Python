def human_to_dog_years(human_years):
    if human_years < 0:
        return "Ошибка: возраст не может быть отрицательным."
    elif human_years <= 2:
        return human_years * 10.5
    else:
        return 2 * 10.5 + (human_years - 2) * 4

# Запрос у пользователя возраста собаки
human_years = float(input("Введите возраст собаки в человеческих годах: "))

# Пересчет возраста и вывод результата
result = human_to_dog_years(human_years)
print(f"Возраст собаки в собачьих годах: {result}")
