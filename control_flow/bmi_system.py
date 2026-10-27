def bmi_calculation( ):
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    if height == 0:
        return "height cannot be 0"

    bmi = weight / (height * height)

    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "healthy weight"
    elif bmi < 30:
        return "overweight"

    return bmi

print(bmi_calculation())
