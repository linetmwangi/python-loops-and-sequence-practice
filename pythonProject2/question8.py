def keys_greater_than(dictionary, n):
    result = [key for key, value in dictionary.items() if value > n]
    return result

print(keys_greater_than({'a': 5, 'b': 12, 'c': 3}, 4))  # Output should be ['a', 'b']
