def get_days_in_month(month):
    month = month.lower()
    days_in_month = {
        "january": 31, "march": 31, "may": 31, "july": 31,
        "august": 31, "october": 31, "december": 31,
        "april": 30, "june": 30, "september": 30, "november": 30,
        "february": "28 или 29"
    }
    return days_in_month.get(month, "Ошибка: некорректное название месяца.")

# Запрос у пользователя названия месяца
month = input("Введите название месяца: ")

# Определение и вывод количества дней в месяце
result = get_days_in_month(month)
print(f"В месяце {month.capitalize()} {result} дней.")
