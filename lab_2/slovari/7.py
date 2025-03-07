def is_phrase_anagram(phrase1, phrase2):
    import re
    clean1 = re.sub(r'[^a-zA-Z]', '', phrase1).lower()
    clean2 = re.sub(r'[^a-zA-Z]', '', phrase2).lower()
    return sorted(clean1) == sorted(clean2)

p1 = input("Enter first phrase: ")
p2 = input("Enter second phrase: ")
print("Anagrams" if is_phrase_anagram(p1, p2) else "Not anagrams")