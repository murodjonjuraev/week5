def full_name(first, last):
    """return full name"""
    # print(f"{first.title()} {last.title()}")
    return f"{first.title()} {last.title()}"


name = full_name('john', 'doe')
print(f"{name}, Welcome to the class")


def adding(a, b):
    return a + b


total = adding(333, 333)
print(total)
print(f"total is {adding(555, 555)}")


def full_name_dict(first, last):
    """return dictionary with first name  full name"""
    # print(f"{first.title()} {last.title()}")
    result = {"firs_name": first, "last_name": last}
    return result


student1 = full_name_dict("tatiana", "shark")
print(student1)

nums = [5, 55, 76, 1, -9, 0, 1, 456]


def find_one(num_list, number):
    for num in num_list:
        if num == number:
            print(f"{number} is found")
            break


find_one(nums, 1)


def desc_pizza(*toppings):
    print("wh have only choose pizza with following toppings")
    print(*toppings)


desc_pizza("chicken")
desc_pizza("bbq", "mushroom", "pepperoni", "chicken")

print("hello, 45", ["john", "doe"], "world")
