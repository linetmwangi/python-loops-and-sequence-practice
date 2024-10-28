def print_even_value_keys(dictionary):
    for key, value in dictionary.items():
        if value % 2 == 0:
            print(key)

sample_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_value_keys(sample_dict)  # Output should be 'a' and 'c'
