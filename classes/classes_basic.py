# Classes - chapter 9

class Dog():
    """this  is the general class about dog"""
    breed = 'bulldog'
    name = 'brownie'

    def __init__(self, name, age): # initializing class, constructor
        self.name = name
        self.age = age

    # behaviour, method
    def bark(self):
        print("wouf wouf!!")


dog1 = Dog()
dog1.breed = "German shepard"
dog1.name = "rex"
dog1.bark()

dog2 = Dog()
dog2.breed = "pudle"
dog2.name = "bobik"
dog2.bark()

print('name of dog1', dog1.name)
print('breed of dog1', dog1.breed)
dog1.bark()

print('name of dog1', dog2.name)
print('breed of dog1', dog2.breed)
dog2.bark()


class NewDog():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{name.title()} is {self.age} years old.")

    # Behaviour, methods
    def bark(self):
        print(f'{self.name} is barking now')

    def get_name(self):
        print(self.name)


dog3 = NewDog("Sharik", 4)
dog3.bark()
dog3.get_name()

dog4 = NewDog("sharik", 15)
dog4.bark()
dog4.get_name()