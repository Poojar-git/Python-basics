#A dictionary is an unordered (in older versions), mutable (changeable) collection of data that stores values as key-value pairs.

student = {
    "name":"Pooja",
    "age":22,
    "city":"Bangalore"
}
student["age"]=23 #Updating the value of a key
print(student)
print(student["name"]) #Output: Pooja
print(student.get("city")) #Output: Bangalore
print(student["age"])
student["Country"]="India" #Adding a new key-value pair
print(student)
#Removing Items
#1.pop()
student.pop("age")
print(student) #Output: {'name': 'Pooja', 'city': 'Bangalore', 'Country': 'India'}
#del
del student["city"]
print(student) #Output: {'name': 'Pooja', 'Country': 'India'}
#2.clear():Removes all items from the dictionary.   
student.clear()
print(student) #Output: {}  
#3.popitem():Removes the last inserted key-value pair.
student = {
    "name":"Pooja",
    "age":22
}

student.popitem()

print(student)

#Important Dictionary Methods
#1. keys(): Returns a view object that displays a list of all the keys in the dictionary.
student = {
    "name":"Pooja",
    "age":22
}

print(student.keys())
#2. values(): Returns a view object that displays a list of all the values in the dictionary.
print(student.values())
#3. items(): Returns a view object that displays a list of dictionary's key-value tuple pairs.
print(student.items())
#4. update(): Updates the dictionary with the specified key-value pairs.
student.update({"age":23, "city":"Bangalore"})
print(student)
#5. copy(): Returns a shallow copy of the dictionary.
student_copy = student.copy()   

