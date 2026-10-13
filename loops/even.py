def sum_even_numbers(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

result = sum_even_numbers([1 , 2 , 3 , 4 , 5 , 6])
print(result)

