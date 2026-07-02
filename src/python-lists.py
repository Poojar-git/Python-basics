#A list is an ordered, mutable (changeable) collection in Python that can store multiple items of different data types. Lists are created using square brackets [].
shopping = ["Apple", "Milk", "Bread"]
data = ["Pooja", 22, 90.5, True]
print(data)
#Accessing list items: You can access individual items in a list using their index, which starts at 0 for the first item. For example, `shopping[0]` will return "Apple".
print(shopping[0]) #Output: Apple
fruits = ["Apple", "Banana", "Mango"]

print(fruits[-1]) #Output: Mango
#Slicing: You can return a range of items by using the slice syntax. For example
print(fruits[0:2]) #Output: ['Apple', 'Banana']
#Changing Elements
fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"
print(fruits)

#List Methods
#1. append():Adds one item at the end.
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Jackfruit")
print(fruits) #Output: ['Apple', 'Banana', 'Mango', 'Jackfruit']
#2. insert():Adds one item at the specified index.
fruits = ["Apple", "Banana", "Mango"]
fruits.insert(1, "Jackfruit")
print(fruits) #Output: ['Apple', 'Jackfruit', 'Banana', 'Mango']
#3. remove():Removes by value.
fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
print(fruits) #Output: ['Apple', 'Mango']
#4.extend: Adds multiple items from another iterable.
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1) #Output: [1, 2, 3, 4, 5, 6]
#5. pop():Removes by index and returns the removed item.
fruits = ["Apple", "Banana", "Mango"]
fruits.pop(1)
print(fruits) #Output: ['Apple', 'Mango']
#6. clear():Removes all items from the list.
fruits = ["Apple", "Banana", "Mango"]
fruits.clear()  
print(fruits) #Output: []
#7. sort(): Sorts the list in ascending order.
numbers = [3, 1, 4, 2]
numbers.sort(reverse=True) #Sorts in descending order
print(numbers) #Output: [1, 2, 3, 4]
#8. reverse(): Reverses the order of the list.
numbers = [1, 2, 3, 4]  
numbers.reverse()
print(numbers) #Output: [4, 3, 2, 1]
#9. count(): Returns the number of occurrences of a specified value.
fruits = ["Apple", "Banana", "Mango", "Apple"]  
fruits_count = fruits.count("Apple")
print(fruits_count) #Output: 2
#10. index(): Returns the index of the first occurrence of a specified value.   
fruits = ["Apple", "Banana", "Mango"]
index_of_banana = fruits.index("Banana")    
print(index_of_banana) #Output: 1