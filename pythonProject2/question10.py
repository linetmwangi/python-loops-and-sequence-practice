def tuples_to_dict(tuples_list):
    return {key: value for key, value in tuples_list}

print(tuples_to_dict([("apple", 5), ("banana", 3), ("cherry", 7)]))
# Output should be {'apple': 5, 'banana': 3, 'cherry': 7}
