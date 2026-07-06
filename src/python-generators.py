#Accessing using loop
# def numbers():
#     yield 1
#     yield 2
#     yield 3
# for i in numbers():
#     print(i)

#using next()
# def numbers():
#     yield 1
#     yield 2
#     yield 3
# g=numbers()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) #StopIteration

# def demo():
#     print("One")
#     yield 1
#     print("Two")
#     yield 2
#     print("Three")
#     yield 3
# g=demo()
# print(next(g))
# print(next(g))
# print(next(g))

#Generator with loop
# def even():
#     for i in range(2, 22, 2):
#         yield i
# for i in even():
#     print(i)

# numbers=[i*i for i in range(5)]
# print(numbers)

# numbers=(i*i for i in range(5))
# for i in numbers:
#     print(i)

#Generate 1-100 using generator
# def generator():
#     for i in range(1, 101):
#         yield i
# numbers=generator()
# for num in numbers:
#     print(num)

# def numbers():
#     for i in range(1, 101):
#          yield i
# for i in numbers():
#     print(i)

#even numbers between 1-50
# def even_numbers():
#     for i in range(1, 51):
#         if i%2==0:
#             yield i
# for i in even_numbers():
#     print(i)

#first 10 square numbers
# sq=(i*i for i in range(1, 11))
# for i in sq:
#     print(i)

# Reading lines line by line
# def read_file(filename):
#     with open(filename, "r") as file:
#         for line in file:
#             yield line

# data=read_file("student.txt")

# for line in data:
#     print(line)

# #fibonacci
# def fibonacci(n):
#     a, b=0, 1
#     for i in range(n):
#         yield a
#         a, b=b, a+b
# for i in fibonacci(10):
#     print(i)

# def numbers():
#     for i in range(1, 11):
#         yield i
# for i in numbers():
#     print(i)
    
# numbers=[i*i for i in range(11)]
# for i in numbers:
#     print(i)

# numbers=(i*i for i in range(1, 11))
# for i in numbers:
#     print(i)

# def even_num():
#     for i in range(1, 11):
#         if i%2==0:
#             yield i
# for i in even_num():
#     print(i)

# def fibonacci(n):
#     a,b=0,1
#     for i in range(1, n+1):
#         yield a
#         a,b=b,a+b
# for i in fibonacci(3):
#     print(i)

# def fibonacci(n):
#     n1,n2=0,1
#     for i in range(n):
#         print(n1, end=" ")
#         n1, n2=n2, n1+n2
# fibonacci(5)


