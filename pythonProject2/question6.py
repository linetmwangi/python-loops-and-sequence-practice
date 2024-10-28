def largest_in_tuple(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(largest_in_tuple((10, 20, 30, 40, 50)))  # Output should be 50
