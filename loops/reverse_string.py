def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

result = find_largest([12, 5, 8, 20, 15])
print(result)