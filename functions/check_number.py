def check_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"

    return "zero"

print(check_number(0))
print(check_number(10))
print(check_number(-5))