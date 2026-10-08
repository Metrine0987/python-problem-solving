number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))

if number1 > number2:
    print(f"{number1} greater than the second number")
elif number1 < number2:
    print(f"{number2} is greater than the first number")
else:
    print("They are equal")