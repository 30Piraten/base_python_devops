class FancyCar():
    # add a class variable
    wheels = 4
    # add a method | a method is a function
    def driveFast(self):
        print("Driving too fast")

# Instantiate a fancy car
my_car = FancyCar()

# access the class attribute
result = my_car.wheels
print(result)

# invoke the method
my_car.driveFast()
