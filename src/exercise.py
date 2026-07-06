# purchase_amount=10000
# if purchase_amount > 5000:
#     discount = 0.10 * purchase_amount
#     print(discount)
# else:
#     print(discount)

# string = "hi"
# reverse=""
# for char in string:
#     reverse=char+reverse
# print(reverse)

# #nested list: to split nested list
# list1=[[1,2],[1,2,3]]
# for i in list1:
#     for j in i:
#         print(j)

# d1={"name":"pooja"}
# d2={"name":"pooja"}
# d3={**d1,**d2}
# print(d3)
# #A company gives a bonus of ₹5,000 to employees whose salary is less than ₹30,000. Store employee details using variables and calculate the updated salary.
# salary=20000
# bonus=5000
# if(salary<30000):
#     updated_salary=salary+bonus
# print(updated_salary)

#Store a student's name, age, marks, and whether they passed.
# name = input("Enter name:")
# age=input("Enter age:")
# marks=input("Enter marks:")
# passed=True
# print(name+" "+age+ " "+ marks+" ")
# print(passed)

#Store temperature in Celsius and convert it to Fahrenheit.
# celsius=20
# fahrenheit=(celsius*9/5)+32
# print(fahrenheit)

# fahrenheit=68
# celsius=(fahrenheit-32)*5/9
# print(celsius)

#Swap two numbers
# a=2
# b=3
# a,b = b, a
# print("a:",a)
# print("b:",b)

# #Find the datatype
# a=10
# print(type(a))

#Simple interest
# p=10000
# t=20
# r=2
# s_i=(p*t*r)/100
# print(s_i)

#Customer wants to withdraw money. If the balance is enough, allow withdrawal.
# withdrawal_amount=50000
# balance=10000
# if withdrawal_amount<=balance:
#     print("allow")
#     balance=balance-withrawal_amount
#     print(balance)
# else:
#     print("dont allow")

#voting elibility
# age = 20
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible")

# Student Grade
# marks = 30
# if marks>=90:
#     print("Grade A")
# elif marks>=80:
#     print("grode b")
# else:
#     print("grade c")

# Login System
# username=input("Enter the username:")
# password=input("Enter the password:")
# if username=="admin" and password=="123":
#     print("Login successful")
# else:
#     print("Login failed")

#Largest of three numbers
# a=2
# b=3 
# c=4
# if a>b and a>c:
#     print("a is greater")
# elif b>c:
#     print("b is greater")
# else:
#     print("c is greater")

#Check even or odd
# a=10
# print(a%2==0)

#Check leap year
# year=2026
# if (year % 400==0) or (year % 4==0 and year %100!=0):
#     print("Leap year")
# else:
#     print("Not a leap year")

#Allow only 3 login attempts
# count =1
# while count<=3:
#     print("Attempt", count)
#     count+=1
# else:
#     print("Attempt failed")

#Set a count down
# count = 10
# while count >=1:
#     print(count)
#     count-=1
# print("Timeup")

#Multiplication table
# num=7
# for i in range(1, 11):
#     print(num*i)

#Store biling
# products=[100, 200, 300, 400]
# total=0
# for i in products:
#     total+=i
# print(total)

#print 1 to 10
# i =1
# while i <=10:
#     print(i)
#     i+=1

#sum of first 10 numbers
# i=1
# sum=0
# while i <=10:
#     sum+=i
#     i+=1
# print(sum)

#reverse a string
# string="pooja"
# reverse=""
# for ch in string:
#     reverse=ch+reverse
# print(reverse)

#count the vowels
# word="Pooja"
# count=0
# for ch in word:
#     if ch.lower() in "aeiou":
#         count+=1
# print(count)

#Find maximum in list
# list1=[2, 3, 9, 60, 90]
# maximum=list1[0]
# for i in list1:
#     if i>maximum:
#         maximum=i
# print(i)

#removing duplicates
# num=[4, 1, 2, 2, 3, 4]
# result=[]
# for n in num:
#     if n not in result:
#         result.append(n)
# print(result)

#count frequency of characters
# msg="apple"
# count=0
# for i in msg:
#     print(i, "=", msg.count(i))

#check for a palindrome
# string="madam"
# reverse=""
# for ch in string:
#     reverse=ch+reverse
# if string==reverse:
#     print("Palidrome")
# else:
#     print("Not palindrome")

# Minimum in list
# list1=[1, 2, 7, 0, 9]
# minimum=list1[0]
# for i in list1:
#     if i < minimum:
#         minimum=i
# print(minimum)

#nested list: to combine into single list
# list1=[[1,2], [1,2,3]]
# result=[]
# for i in list1:
#     for j in i:
#         result.append(j)
# print(result)

#Factorial
# def fact(num):
#     if num == 1 or num==0:
#         return 1
#     else:
#         return num*fact(num-1)
# factorial=fact(2)
# print(factorial)

#Reverse a number
# num=12345
# reverse=0
# while num > 0:
#     digit= num%10
#     reverse=reverse*10+digit
#     num = num //10
# print(reverse)

# num=1200
# reverse=""
# while num>0:
#     digit=num%10
#     reverse= reverse+str(digit)
#     num=num//10
# print(reverse)

#prime numbers
# n=3
# if n<2:
#     print("Not Prime")
# else:
#     for i in range(2, n):
#      if n%i==0:
#        print("Not prime")
#        break
#     else:
#         print("Prime")

n=200
# if n<2:
#     print("Not prime")
# else:
#     prime=True

#     for i in range(2, n):
#         if n%i==0:
#             prime=False
#             break
# if prime:
#     print("Prime")
# else:
#     print("Not prime")

# list1=[1, 2, 3, 1, 4]
# num=1
# count=0
# for i in list1:
#     if num==i:
#         count+=1
# print(count)