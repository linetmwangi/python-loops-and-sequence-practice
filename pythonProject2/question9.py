def has_pair_with_sum(lst, target_sum):
    seen = set()
    for num in lst:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)
    return False

print(has_pair_with_sum([1, 2, 3, 4, 5], 9))  # Output should be True (4 + 5)
print(has_pair_with_sum([1, 2, 3, 4, 5], 10))  # Output should be False
