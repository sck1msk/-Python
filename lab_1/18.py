def check_letter(letter):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if letter.lower() == 'y':
        return "Буква 'y' может быть как гласной, так и согласной."
    elif letter.lower() in vowels:
        return f"Буква '{letter}' является гласной."
    else:
        return f"Буква '{letter}' является согласной."

# Запрос у пользователя буквы
letter = input("Введите букву латинского алфавита: ").strip()

if len(letter) != 1 or not letter.isalpha():
    print("Ошибка: введите одну букву латинского алфавита.")
else:
    result = check_letter(letter)
    print(result)

