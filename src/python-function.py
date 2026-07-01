#A function is a block of code which only runs when it is called.
#A function helps avoiding code repetition.

def my_function():
    print("Hello from a function")
my_function()
#A function name must start with a letter or underscore
#A function name can only contain letters, numbers, and underscores
#Function names are case-sensitive (myFunction and myfunction are different)
#return values: A function can return a value as a result. To let a function return a value, use the return statement.
def my_func():
    return "Greetings"
msg=my_func()
print(msg)
#pass parameters: Information can be passed into functions as parameters. Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.
def my_function():
    pass
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with +.
def my_function(fname):
  print(fname + " Refsnes" + " poo")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#A parameter is the variable listed inside the parentheses in the function definition.

#An argument is the actual value that is sent to the function when it is called.
def myfunc(name):
    print("Hello, "+name)
myfunc("Pooja")
#Default Parameter Values
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
#Keyword Arguments: key=value
def myfunc(animal, name):
    print("My " +animal+"'s name is "+name)
myfunc(animal="dog", name="puppy")
#Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
#Mixing positional and keyword arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)
#*args and **kwargs allow functions to accept a unknown number of arguments.
#If you do not know how many arguments will be passed into your function, add a * before the parameter name.
def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")

def my_function(greeting, *names):
    print(greeting,  names[0])

my_function("Hello", "Emil", "Tobias", "Linus")
#If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")