def reverse_strings(strings):
    reversed_list = [s[::-1] for s in strings]
    return reversed_list

print(reverse_strings(["apple", "banana", "cherry"]))  # Output should be ["elppa", "ananab", "yrrehc"]
