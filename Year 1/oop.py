import os
os.system('clear')

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
my_first_car = Car('Audi', 'a4', 2016)
my_second_car = Car('Skoda', 'Kodiac', 2023)

print(my_first_car.make)
print(my_second_car.model)

my_first_car.odometer_reading = 23
print(my_first_car.odometer_reading)