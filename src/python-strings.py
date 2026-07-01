#Strings are sequences of characters used to represent text in programming. In Python, strings are enclosed in either single quotes (' ') or double quotes (" "). They can contain letters, numbers, symbols, and whitespace. Strings are immutable, meaning that once they are created, their content cannot be changed. Python provides various methods and operations to manipulate strings, such as concatenation, slicing, and formatting.
print("Hello")
#Quotes inside quotes
print("Hello 'Good Morning'")
#Assign string to a varaible
a= "Greeting"
print(a)
#Multiline string
a = """This is a multiline string.
It can span multiple lines."""
print(a)
#Note: in the result, the line breaks are inserted at the same position as in the code.
#Strings are arrays of bytes representing unicode characters
message="Have a nice day"
print(message[2]) #Accessing characters in a string
#Looping through strings
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#Length of string
product="laptop"
print(len(product))
#check string
address="I live in bangalore"
print("bangalore" in address)
#using if check
if "bangalore" in address:
    print("Yes, 'bangalore' is present.")
#Check if not
if "Delhi" not in address:
    print("Delhi, is not in address")
#or
print("Delhi" not in address)
#Slicing: You can return a range of characters by using the slice syntax.
a="Welcome to Python"
print(a[1:3])
#Modify Strings
a=" pooja r"
print(a.upper()) #Convert to uppercase
print(a.lower()) #Convert to lowercase
print(a.strip()) #Remove whitespace from the beginning or end
print(a.replace('p', 'r')) #Replace a character with another
print(a.split(',')) #Split a string into a list
#string concatenation
a="Hello"
b="World"
print(a+" "+b)
#String formatting: You can use the format() method to insert values into a string.
age = 36
#This will produce an error:
txt = f"My name is John, I am  {age}"
print(txt)

