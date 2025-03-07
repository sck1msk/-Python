def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

w1 = input("Enter first word: ")
w2 = input("Enter second word: ")
print("Anagrams" if is_anagram(w1, w2) else "Not anagrams")