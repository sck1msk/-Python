def reverseLookup(dictionary, value):
    return [key for key, val in dictionary.items() if val == value]

if __name__ == "__main__":
    sample_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
    print(reverseLookup(sample_dict, 1))  # ['a', 'c']
    print(reverseLookup(sample_dict, 2))  # ['b']
    print(reverseLookup(sample_dict, 4))  # []