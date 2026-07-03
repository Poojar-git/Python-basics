# file = open("student.txt", "r")
# print(file.read())
# file.close()

# file=open("student.txt", "w")
# file.write("Pooja")
# file.close()

# file = open("student.txt", "a")
# file.write("\nRahul")
# file.close()

# file=open("new.txt", "x")

# file = open("student.txt", "w")
# file.write("\nProduct")
# file.write("\nOwner")
# file.close()

# with open("student.txt", "a") as file:
#     file.write("\nLaptop")

# with open("student.txt", "r") as file:
#     # lines = file.readlines()
#     text = file.read()
#     words=text.split()
#     print(len(words))
#     # print(len(lines))

# with open("student.txt", "r") as file:
#     text = file.read()
# print(len(text))

# import os
# if os.path.exists("student.txt"):
#     print("File exists")
# else:
#     print("Not exists")

# import os
# os.rename("student.txt", "student-data.txt")
# print("Rename successful")

# import os
# os.remove("new.txt")
# print("File deleted")

# import os
# os.mkdir("Reports")

# import os
# os.rmdir("Reports")

# import os
# print(os.listdir())

# import os
# print(os.getcwd())

# import os
# os.chdir("C:\\Users\\PoojaR\\Python-basics")

# import shutil
# shutil.copy("student-data.txt", "student_backup.txt")

# import shutil
# shutil.move("student-data.txt", "Reports/")

# import shutil
# shutil.copytree("Reports", "Reports_Backup")

# import shutil
# shutil.rmtree("Reports_backup")