a = 33
b = 200
if b > a:
  print("b is greater than a")
# If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.
#Using Variables in Conditions
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
#0, "", None->false, while numbers, negative numbers"False" -> True
x = 2
y = 3
z = 5
if x>y and x>z:
    print("x is greater than y and z")
elif y>z:
    print("y is greater than z")
else:
    print("c is the greatest")
#Shorthand if
p=9
if p<10: print("p is less than 10")
o=2
print(o) if o<=2 else print('o is greater than 2')#Shorthand if else
#assign a value with if else
y=100
x=20 if x>y else 30
print(x, y)
#Multiple conditions in one line
a=330
b=330
print(a) if a>b else  print("b=",b) if a==b else print(a)
#Logical Operatore
a=10
b=20
if a<b and a!=0:
    print("a is less than b and a is not equal to 0")
if a<b or a==0:
    print("a is less than b or a is equal to 0")
if not a<b:
    print("a is greater than b")
#Nested loop
age=20
license=True
if age>=18:
    if license:
        print("You are eligible to drive")
    else:
        print("You are not eligible to drive apply for license")
else:
    print("You are too yung to drive")
#pass 
a = 33
b = 200

if b > a:
    pass#The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.


  
