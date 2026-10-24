number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 >= number2 and number1 >= number3:
    print("number 1 is the largest number")
elif number2 >= number1 and number2 >= number3:
    print("number 2 is the largest")
else:
    print("number 3 is the largest")