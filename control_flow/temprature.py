temperature = int(input("Enter temperature:"))

if temperature > 30:
    print("It's hot")
elif temperature >= 20:
    print("warm")
elif temperature >= 10:
    print("cool")
else:
    print("cold")