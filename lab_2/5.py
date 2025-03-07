def number_to_ordinal(num):

    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
        "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    if 1 <= num <= 12:
        return ordinals[num - 1]
    return ""

print("\nЧислительные для чисел от 1 до 12:")
for i in range(1, 13):
    print(f"{i}: {number_to_ordinal(i)}")