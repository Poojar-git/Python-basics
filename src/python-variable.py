print("Variable")
print("Variable is a name given to the memory location that stores some value")

#Casting is the process of converting a variable from one data type to another data type. In Python, we can cast variables using the following functions:
x=str(2)
y=int(4)
z=float(3)
print(x)
print(y)
print(z)

#Get the Type
print(type(x))
print(type(y))
print(type(z))

#Multi Words Variable Names
#Camel Case
myVariableName = "John"
#Pascal Case
MyVariableName = "John"
#Snake Case
my_variable_name = "John"

#Assign multiple values to multiple variables
a, b, c = "Orange", "Banana", "Cherry"
print(a)
#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global Variables: Variables that are created outside of a function are known as global variables.
x = "nice"

def myfunc():
  print("Python is " + x)
print(x)
myfunc()

#Local Variables: Variables that are created inside a function are known as local variables.
def my_func():
    an='nice'
    print('Python is' + an)
my_func()
#print(an)#error: name 'an' is not defined

#To create a global variable inside a function, you can use the global keyword.
def thefunc():
    global name 
    name = "Pooja"
    print(name)
thefunc()
print(name)

#Also, use the global keyword if you want to change a global variable inside a function.
fruit="apple"
def fruitss():
    global fruit
    fruit="banana"
    print(fruit)
fruitss()