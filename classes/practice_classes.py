class Cat():
    """Creating a Cat class for the first time"""

    def __init__(self, name, color, age):
        """Initializing name, color and age attributes"""
        self.name = name
        self.color = color
        self.age = age
        self.breed = "something"

    def about_cat(self):
        parameters = f"\nAll about cats: \n\tCat's name: {self.name.title()} \n\tCat's color: {self.color.title()} \n\tCat's age: {self.age}\n\tBreed: {self.breed}"
        return parameters

    def sit(self):
        """Simulating cat to listen to our command sit"""
        print(f"{self.name.title()} is listening to our command and sitting")

    def roll_over(self):
        """Simulating cat to rollover"""
        print(f"{self.name.title()} is rolling over")

    def set_breed(self, new_breed):
        self.breed = new_breed

# Home work 9-1, 9-2, 9-4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing restaurat_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def desc_res(self):
        print(f"Name of the restaurant: {self.restaurant_name} it is {self.cuisine_type} cuisine customers served {self.number_served}")

    def open_res(self):
        print("this restaurant open from 10am to 10pm")

    def set_served(self, new_served):
        self.number_served = new_served

# Home work 9-3
class User():

    def __init__(self, first_name, last_name):
        """Initializing first_name and last_name attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = "abc"
        self.age = 20

    def desc_user(self):
        """Here all about this user"""
        print(f"\tF.N: {self.first_name.title()}\n\tL.N:{self.last_name.title()}\n\tEmail: {self.email}\n\tage:{self.age}")

    def greet_user(self):
        print("Hello dear user.")

    def set_email(self, new_email):
        self.email = new_email

    def set_age(self, new_age):
        self.age = new_age



