class Car():
    """This is class to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = "White"
        self.odometer_reading = 0

    # getter(return) and setter(assign new value)
    def get_description(self):
        msg = f"your car:\n\tmanufacturer: {self.make}\n\tModel: {self.model}\n\tYear: {self.year}\n\tColor: {self.color}"
        return msg

    def set_color(self, new_color):
        self.color = new_color

    def read_odmeter(self):
        """gets miles of the car"""
        msg = f"car has {self.odometer_reading} miles on it"
        return msg

    def set_odometer(self, new_miles):
        if new_miles >= self.odometer_reading:
            print(f" Setting odomoeter reading from {self.odometer_reading} to {new_miles}")
            self.odometer_reading = new_miles
        else:
            print(f"you can not roll back odometer.")

    def increment_odometer(self, miles):
        """Adding :param miles to odometer_reading"""
        # self.odometer_reading = self.odometer_reading + miles
        if miles > 0:
            print(f"Incrementing odometer with more {miles} miles.")
            self.odometer_reading += miles
        else:
            print(f"Negative value can not be passed to odometer : {miles}.")



class ElectricCar(Car):
    """represents electric car inrerets all features of car"""

    def __init__(self, make, model, year, battery_size): # Overriding
        """child class constractor, Overriding the parent constructor"""
        super().__init__(make, model, year) # calling constructor of parent class
        self.battery_size = battery_size

    def get_description(self):
        msg = f"your car:\n\tmanufacturer: {self.make}\n\tModel: {self.model}\n\tYear: {self.year}\n\tColor: {self.color}\n\tBattery size: {self.battery_size}"
        return msg

    def test_method(self):
        print(self.get_description()) # current class get_description()
        print(super().get_description()) # parent class get_description()