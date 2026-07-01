#A set is an unordered, mutable collection of unique elements. It does not allow duplicate values and is created using curly braces {} or the set() constructor.

# Set = Unique values only
fruits = {"Apple", "Banana", "Mango"}
print(fruits)
numbers = {1,2,2,3,3,4}
print(numbers)
#Empty set: To create an empty set, you need to use the set() constructor. Using {} will create an empty dictionary instead.
empty_set = set()
print(empty_set)
#Sets do not support indexing.
#If you want to access elements:
for num in numbers:
    print(num)
#Adding Elements
#1. add(): Adds one element.
fruits = {"Apple","Banana"}
fruits.add("Mango")
print(fruits)
#2. update(): Adds multiple elements from another iterable (like a list, tuple, or set).
fruits = {"Apple","Banana"}
fruits.update(["Mango", "Orange"])
print(fruits)
#   Removing Elements
#1. remove(): Removes a specified element. Raises a KeyError if the element is not found.
fruits = {"Apple", "Banana", "Mango"}
fruits.remove("Banana")
print(fruits)
#discard(): Removes a specified element. Does not raise an error if the element is not found.
fruits = {"Apple", "Banana", "Mango"}   
fruits.discard("Banana")
print(fruits)
#pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
fruits = {"Apple", "Banana", "jackfruit", "Mango"}   
removed_element = fruits.pop()
print(removed_element)
#4. clear(): Removes all elements from the set.
fruits = {"Apple", "Banana", "Mango"}
fruits.clear()
print(fruits) #Output: set()

#Important Set Operations
#1. union(): Returns a new set containing all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result) #Output: {1, 2, 3, 4, 5}
#2. intersection(): Returns a new set containing only the elements that are common to both sets.
set1 = {1, 2, 3}        
set2 = {3, 4, 5}
result = set1.intersection(set2)
print(result) #Output: {3}
#3. difference(): Returns a new set containing the elements that are in the first set but not in the second set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2)
print(result) #Output: {1, 2}
#4. symmetric_difference(): Returns a new set containing the elements that are in either of the sets but not in both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)
print(result) #Output: {1, 2, 4, 5} 

#Frozenset: A frozenset is an immutable version of a set. Once created, you cannot add or remove elements from it. Frozensets are created using the frozenset() constructor.
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)
#You cannot add or remove elements from a frozenset.