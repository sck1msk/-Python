def postalCodeInfo(postal_code):
    regions = {
        'A': 'Ньюфаундленд', 'B': 'Новая Шотландия', 'C': 'Остров Принца Эдуарда',
        'E': 'Нью-Брансуик', 'G': 'Квебек', 'H': 'Квебек', 'J': 'Квебек',
        'K': 'Онтарио', 'L': 'Онтарио', 'M': 'Онтарио', 'N': 'Онтарио', 'P': 'Онтарио',
        'R': 'Манитоба', 'S': 'Саскачеван', 'T': 'Альберта', 'V': 'Британская Колумбия',
        'X': 'Нунавут и Северо-Западные территории', 'Y': 'Юкон'
    }
    
    if len(postal_code) < 2 or postal_code[0] not in regions or not postal_code[1].isdigit():
        return "Ошибка: некорректный почтовый индекс"
    
    region = regions[postal_code[0]]
    locality = "городская местность" if postal_code[1] != '0' else "сельская местность"
    
    return f"{region}, {locality}"

if __name__ == "__main__":
    user_postal_code = input("Введите почтовый индекс: ")
    print(postalCodeInfo(user_postal_code))
