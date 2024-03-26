def greeting():
    return 'Welcome to Python'


def upper_case_decorator(function):
    def wrapper():
        func = function()
        u = func.upper()
        return u

    return wrapper


g = upper_case_decorator(greeting)
print(g())


def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


# call the 'upper_case_decorator' first
@split_string_decorator
@upper_case_decorator
def greeting2():
    return "welcome to Python"


print(greeting2())
