import random

def generate_bingo_card():
    card = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }
    return card

def display_bingo_card(card):
    print(" B   I   N   G   O")
    for i in range(5):
        print(" ".join(f"{card[col][i]:2}" for col in "BINGO"))

def check_bingo_win(card):
    # Проверка горизонтальных линий
    for row in range(5):
        if all(card[col][row] == 0 for col in "BINGO"):
            return True
    
    # Проверка вертикальных линий
    for col in "BINGO":
        if all(num == 0 for num in card[col]):
            return True
    
    # Проверка диагоналей
    if all(card[col][i] == 0 for i, col in enumerate("BINGO")):
        return True
    if all(card[col][4 - i] == 0 for i, col in enumerate("BINGO")):
        return True
    
    return False

def mark_numbers(card, numbers):
    for col in "BINGO":
        card[col] = [0 if num in numbers else num for num in card[col]]
    return card

# Генерация и проверка примеров
bingo_card = generate_bingo_card()
display_bingo_card(bingo_card)

test_numbers = set()
for col in "BINGO":
    test_numbers.add(bingo_card[col][random.randint(0, 4)])

bingo_card = mark_numbers(bingo_card, test_numbers)
display_bingo_card(bingo_card)

if check_bingo_win(bingo_card):
    print("Выигрышная карточка!")
else:
    print("Не выиграла.")
