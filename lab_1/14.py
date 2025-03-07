def height_to_cm(feet, inches):
    cm_per_inch = 2.54
    inches_total = feet * 12 + inches
    return inches_total * cm_per_inch

# Запрос у пользователя роста в футах и дюймах
feet = int(input("Введите количество футов: "))
inches = int(input("Введите количество дюймов: "))

if feet < 0 or inches < 0:
    print("Рост не может быть отрицательным.")
else:
    height_cm = height_to_cm(feet, inches)
    print(f"Ваш рост в сантиметрах: {height_cm:.2f} см")
