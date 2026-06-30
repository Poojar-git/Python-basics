print("Data Type")
print("A data type defines the type of a data variable is storing")

#get the type of a variable
x=True
print(type(x))

#setting the data type
x="Hello World" #str
x=20#int
x=20.0#float
x=1j#complex
x=['a', 'b', 'c']#list
x={'name':'John', 'age':36}#dict
x={'fruit', 'veggies', 'meat'}#set
x=range(6)#range
x=("apple", "banana", "cherry")#tuple
x=frozenset({"apple", "banana", "cherry"})#frozenset
x=True#bool
x=b"Hello"#bytes
x=bytearray(5)#bytearray
x=memoryview(bytes(5))#memoryview   
x=None#NoneType