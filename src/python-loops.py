#for loop: A for loop is used for iterating over a sequence
fruits=["apple", "banana", "cherry", "jackfruit"]
for x in fruits:
    print(x)
for x in "banana":
    print(x)
#break: stop the loop before it has looped through all the items
fruits=["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        break
    print(x)
#continue: skip the current iteration and continue with the next
fruits=["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)
#range(): The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
for x in range(1,11, 2):
    print(x)
#Else in for
for x in range(6):
    print(x)
    if x==3:
        break
else:
    print("Finished!")#Note: The else block will NOT be executed if the loop is stopped by a break statement.
#Nested loops
a=[1,2,3]
b=["x", "y", "z"]
for c in a:
    for d in b:
        print(c, ",", d)

#While loops:With the while loop we can execute a set of statements as long as a condition is true.
i=1
while i<10:
    print(i)
    i+=1
    if i==3:
        break
else:
    print("Finished!")#Note: The else block will NOT be executed if the loop is stopped by a break statement.
    

