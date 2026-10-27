class Car:
    def __init__(self , model , colour , year):
        self.model = model
        self.colour = colour
        self.year = year

    def drive(self):
        print("You drive the car")

    def stop(self):
        print("Stop the car")