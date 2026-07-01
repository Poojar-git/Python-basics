#A tuple is an ordered, immutable collection in Python that can store multiple items of different data types. Tuples are created using parentheses ().
fruits = ("Apple", "Banana", "Mango")

print(fruits)
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])#Accessing tuple items: You can access individual items in a tuple using their index, which starts at 0 for the first item. For example, `fruits[0]` will return "Apple".
fruits = ("Apple", "Banana", "Mango")

print(fruits[1:3])#Slicing: You can return a range of items by using the slice syntax. For example, `fruits[1:3]` will return ("Banana", "Mango").
#Creating  a tuple
#Empty tuple: 
Empty_tuple = ()#allowed
#Tuple with one item:
single_item_tuple = (10)#allowed but considers it as an integer, not a tuple. To create a single-item tuple, you need to include a comma after the item, like this: `single_item_tuple = (10,)`.
print(type(single_item_tuple))
tuple_with_one_item = (10,)
print(type(tuple_with_one_item))#cosidering it as a tuple
#Tuple Methods
#1. count()
fruits = ("Apple", "Banana", "Mango", "Apple")
apple_count = fruits.count("Apple")
print(apple_count)
#2. index()
fruits = ("Apple", "Banana", "Mango")
index_of_banana = fruits.index("Banana")
print(index_of_banana)
