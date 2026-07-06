# square every number
# numbers=[1,2,3,4,5]
# square=map(lambda x:x*x, numbers)
# print(list(square))

#Increase every employee's salary by ₹5000.
# employeesSalary=[10000, 20000, 13000, 15000]
# increseSalary=list(map(lambda x:x+5000, employeesSalary))
# print(increseSalary)

#Convert names to uppercase.
# names=["pooja", "sona", "viji"]
# upperCaseWords=list(map(lambda x:x.upper(), names))
# print(upperCaseWords)

# numbers=[1,2,3,4,5,6,7,8]
# even=list(filter(lambda x:x%2==0, numbers))
# print(even)

# Find employees earning more than ₹40,000.
# salary=[30000, 40000, 50000, 10000]
# found=list(filter(lambda x: x>40000, salary))
# print(found)

# Keep names longer than 4 characters.
# names=["pooja", "sona", "viji"]
# found=list(filter(lambda x: len(x)>4, names))
# print(found)

# from functools import 

# Find the sum.
# from functools import reduce
# numbers=[1,2,3,4,5]
# sum=reduce(lambda x,y:x+y, numbers)
# print(sum)

#Largest Number
# from functools import reduce
# numbers=[2,4,6,8,10]
# largest=reduce(lambda x,y: x if x>y else y, numbers)
# print(largest)

