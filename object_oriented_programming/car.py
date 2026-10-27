class Car:
    def __init__(self , model , colour , year):
        self.model = model
        self.colour = colour
        self.year = year

car1 = Car("Mazda" , "white" , 2026)

print(car1.model)