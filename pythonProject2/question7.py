def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output should be [1, 2, 3, 4, 5]
