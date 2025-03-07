def scrabble_score(word):
    scores = {1: "AEILNORSTU", 2: "DG", 3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
    score_dict = {letter: points for points, letters in scores.items() for letter in letters}
    return sum(score_dict.get(letter.upper(), 0) for letter in word)

word = input("Enter a word: ")
print("Scrabble score:", scrabble_score(word))