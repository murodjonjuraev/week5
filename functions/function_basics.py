# functions
import time


def greet_user():
    """Greets to user"""
    print("welcome to class")


def greet_user_1(name):
    """greeting user with name"""
    print(f"welcome to {name.title()}!")


def greet_user_comp(companyname, username):
    """greeting user with name"""
    print(f"{username.title()} welcome to {companyname.upper()}!")


def greet_user_comp2(username, companyname="yahoo", ):
    """greeting user with name"""
    print(f"{username.title()} welcome to {companyname.upper()}!")
    print("Have a great week!")


def greet_user_4(username, company=None):
    if company is None:
        print(f"{username}, welcome to new home")
    else:
        print(f"{username}, welcome to {company}!")
    print("have a great week")


time.sleep(0.5)
comp = "Level up"
greet_user()  # this is execution of the code inside the function >> calling function
greet_user_1("Jungle")  # have to pass name or you will get error message
greet_user_1(comp)
greet_user_comp("google", "inom")
greet_user_comp2("murod")
greet_user_4("vika")
greet_user_4("vika", "bloomberg")


def display_messaage():
    print("We are learning Functions in this chapter")


display_messaage()


def favorite_book(title):
    print("One of my favorite books" + " " + (title.title()))


favorite_book("alice in wonderland")
favorite_book("beauty and the beast")


def make_shirt(size, text):
    print(f"This is {size} size {text} shirt!")


make_shirt("Small", "I love New York")
make_shirt(text="Adidas", size="Medium")


def make_shirt(size="Large", text="I love python"):
    print(f"This is {size} size {text}!")


make_shirt("Small", "Nike")
make_shirt(text="Adidas", size="Medium")
make_shirt()
make_shirt("Medium", "I hate java")


def describe_city(city_name, country="USA"):
    print(f"{city_name} is in {country}")


describe_city("New York")
describe_city("Chicago")
describe_city("Dushanbe", country="tajikistan")
print()


def get_formatted_name(firstname, lastname):
    """Return full name"""
    fullname = firstname + " " + lastname
    return fullname.title()


musician = get_formatted_name("Jimmi", "Hendrix")
print(musician)
print()


def get_formatted_name1(firstname, middlename, lastname):
    """Return full name"""
    fullname = firstname + " " + middlename + " " + lastname
    return fullname.title()


musician = get_formatted_name1("John", "lee", "hooker")
print(musician)
print()


def get_formatted_name2(firstname, lastname, middlename=""):
    """Return full name"""
    if middlename:
        fullname = firstname + " " + middlename + " " + lastname
    else:
        fullname = firstname + " " + lastname
    return fullname.title()


musician = get_formatted_name2("Jimi", "Hendrix")
print(musician)
musician = get_formatted_name2("John", "hooker", "lee")
print(musician)
print()


def build_person(firs_name, last_name):
    """return a dictiobary og info about person"""
    person = {"first": firs_name.title(), "last": last_name.title()}
    return person


musician = build_person("jimi", "hendrix")
print(musician)
print()


def build_person(firs_name, last_name, age=""):
    """return a dictiobary og info about person"""
    person = {"first": firs_name.title(), "last": last_name.title()}
    if age:
        person['age'] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)
print()


def get_formatted_name(firstname, lastname):
    """Return full name"""
    fullname = firstname + " " + lastname
    return fullname.title()
# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' any time to quit)")

    f_name = input("first name: ")
    if f_name == 'q':
        break
    l_name = input("last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


def city_country(city, country):
    country_city = city + ", " + country
    return country_city.title()


mmm = city_country('"Santiago"', '"chile"')
print(mmm)



