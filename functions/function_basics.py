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


def greet_user_comp2(username, companyname="yahoo",):
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