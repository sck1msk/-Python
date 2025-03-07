import random

def rollDice():
    return random.randint(1, 6) + random.randint(1, 6)

def simulateRolls(num_rolls=1000):
    results = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        roll = rollDice()
        results[roll] += 1
    
    for outcome in sorted(results.keys()):
        percentage = (results[outcome] / num_rolls) * 100
        expected = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}
        print(f"{outcome}: {percentage:.2f}% (Ожидаемый: {expected[outcome]:.2f}%)")

if __name__ == "__main__":
    simulateRolls()
