def calculator( ):
    operation = input("Choose your operation (+. - ,/,*):")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))


    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0 :
            return "Cannot be divided by 0"
        else:
            return num1 / num2
    else:
        return "Invalid operator"


print(calculator())
