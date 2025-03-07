def convert_feet(feet):
    inches = feet * 12  # 1 фут = 12 дюймов
    yards = feet / 3  # 1 ярд = 3 фута
    miles = feet / 5280  # 1 миля = 5280 футов
    return inches, yards, miles

# Запрос у пользователя расстояния в футах
feet = float(input("Введите расстояние в футах: "))

if feet < 0:
    print("Расстояние не может быть отрицательным.")
else:
    inches, yards, miles = convert_feet(feet)
    print(f"{feet} футов равно:")
    print(f"- {inches:.2f} дюймов")
    print(f"- {yards:.2f} ярдов")
    print(f"- {miles:.6f} миль")
