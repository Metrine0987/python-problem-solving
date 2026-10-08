number1 = int(input("Enter the first number"))
number2 = int(input("Enter the second number"))
operator = input("Enter operational symbol")


if operator == "+" :
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    if number2 == 0:
        print("cannot divide")
    else:
        print(number1 / number2)
else:
    print("Invalid operator")
