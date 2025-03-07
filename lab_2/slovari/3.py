def textToKeypress(text):
    keypad = {
        '1': '.,?!:', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO',
        '7': 'PQRS', '8': 'TUV', '9': 'WXYZ', '0': ' '
    }
    mapping = {char: str(key) * (idx + 1) for key, chars in keypad.items() for idx, char in enumerate(chars)}
    
    text = text.upper()
    return ''.join(mapping.get(char, '') for char in text)

if __name__ == "__main__":
    user_input = input("Введите текст: ")
    print(textToKeypress(user_input))
