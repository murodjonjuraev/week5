# Classes - chapter 9

class Dog():
    """this  is the general class about dog"""
    breed = ''
    name = ''

    # behaviour, method
    def bark(self):
        print("wouf wouf!!")


mydog = Dog()
mydog.breed = "German shepard"
mydog.name = "rex"
mydog.bark()
