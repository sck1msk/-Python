
def number_to_words(n):
    ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    
    if n in ones:
        return ones[n]
    elif n in teens:
        return teens[n]
    elif n < 100:
        return tens[n // 10 * 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
    else:
        return ones[n // 100] + " hundred" + (" " + number_to_words(n % 100) if n % 100 != 0 else "")

num = int(input("Enter a number (0-999): "))
print(number_to_words(num))