from classes.cars import Car, ElectricCar

car1 = Car("toyota", "camry", 2020)
print(car1.get_description())
car1.set_color("red")
print(car1.get_description())
print(car1.read_odmeter())
car1.odometer_reading = 1000 # not good practice
print(car1.read_odmeter())
car1.set_odometer(800)
print(car1.read_odmeter())

car1.set_odometer(1100)
print(car1.read_odmeter())

car1.increment_odometer(-500)
print(car1.read_odmeter())

car1.increment_odometer(400)
print(car1.read_odmeter())

ecar1 = ElectricCar("tesla", "model y", 2020, 100)
print(ecar1.get_description())
ecar1.set_color("Blue")
print(ecar1.get_description())
print("____________________________________")
ecar1.test_method()

# OOP
# - Class, Object
# - Inheritance (single class, multiple class)
# - Constructor (__init__)
# - self keyword, super() method, difference
# - Overrriding(due Inheritance) - rewriting parent attributes/method in child class
# - relatitonship between Parent and child: Parent >> Child
