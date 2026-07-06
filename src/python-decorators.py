#Function are objects
# def greet():
#     print("Hello")
# a=greet
# a()

#Function inside function
# def outer():
#     def inner():
#         print("Inner Function")
#     inner()
# a=outer
# a()

#Returning a function
# def outer():
#     def inner():
#         print("Inner function")
#     return inner()
# a=outer
# a()

#passing function as an argument
# def outer(func):
#     print("Before function")
#     func()
#     print("After function")
# @outer
# def display():
#     print("Display function")

# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper()
# @decorator
# def display():
#     print("Display function")

# def authenticate(func):
#     def wrapper():
#         print("Checking login...")
#         func()
#     return wrapper()
# @authenticate
# def dashboard():
#     print("Dashboard opens")

# def logger(func):
#     def wrapper():
#         print("Function started")
#         func()
#         print("function finished")
#     return wrapper()
# @logger
# def operation():
#     print(10+20)

def admin(func):
    def wrapper():
        print("Permission granted")
        func()
    return wrapper()
@admin
def delete():
    print("Delete the message")

#Decorators with arguments
# def decorator(func):
#     def wrapper(name):
#         print("Before function")
#         func(name)
#         print("After function")
#     return wrapper
# def printt(name):
#     print("Hello", name)
# a=decorator(printt)
# a("Pooja")

# def decorator(fun):
#     def wrapper(*args, **kwargs):
#         print("Before")
#         fun(*args, **kwargs)
#         print("After")
#     return wrapper
# @decorator
# def printt(name, age):
#     print(name," ",age)
# printt("Pooja", 23)

#returning values:
# def decorator(func):
#     def wrapper(a,b):
#         print("Before function")
#         result=func(a,b)
#         print(result)
#         print("After function")
#         return result
#     return wrapper
# @decorator
# def add(a,b):
#     return a+b
# add(2,3)


