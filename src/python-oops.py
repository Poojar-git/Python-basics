# class student:
#     def myfunc(self):
#         print("Hello")
# student1=student()
# student1.myfunc()

# class Employee:
#     def display(pooja):
#         print("Good Morning")
# emp1=Employee()
# emp1.display()

# class Student:
#     def __init__(self):
#         print("Constructor called")
# s1=Student()

# class student:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name)
#         print(self.age)
#     def __str__(self):
#         return(self.name)
# s1=student("Pooja", 22)
# s2=student("sona", 22)
# s1.display()
# s2.display()
# print(s1)

# class animal:
#     def sound(self):
#         print("Animal makes sound")
# class dog(animal):
#     pass
# d1=dog()
# d1.sound()

# class employee:
#     def company(self):
#         print("ABC compay")
# class manager(employee):
#     def department(self):
#         print("IT Company")
# e1=manager()
# e1.company()
# e1.department()

#Duck-typing
# class Dog:
#     def sound(self):
#         print("bark")
# class Cat:
#     def sound(self):
#         print("meow")
# def animal_sound(animal):
#     animal.sound()
# dog=Dog()
# cat=Cat()
# animal_sound(dog)
# animal_sound(cat)

# from abc import abstractmethod, ABC

# class Parent(ABC):
#     def display(self):
#         print("Abstract")
#     @abstractmethod
#     def a(self):
#         print("a")
#     @abstractmethod
#     def b(self):
#         print("b")
# class Child(Parent):
#     def a(self):
#         print("a")
#     def b(self):
#         print("b")
# obj=Child()
# obj.a()
# obj.b()

