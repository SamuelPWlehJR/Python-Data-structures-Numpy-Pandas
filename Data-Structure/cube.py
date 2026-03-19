# cube = [[[0 for col in range(2)]for row in range(3)]for layer in range(2)]
# count = 1
# for layer in range(2):
#    for row in range(3):
#        for col in range(2):
#            cube[layer][row][col] = count
#            count += 1

# for layer in range(2):
#    print(f"\nlayer{layer}:")
#    for row in cube[layer]:
#        print(row)

# from dataclasses import dataclass

# @dataclass
# class Student:
#    id:int
#    name: str
#    age: int
#    gpa: float = 0.0

# s = Student(1, "Ali", 18, 3.2)

# print("Your Name is ", s.name)
# print("Your are ", s.age, "years of age")
# print("Your GPA is ", s.gpa)

# adding a default values

# from dataclasses import dataclass

# @dataclass
# class Product:
#    sku: str
#    name: str
#    price: float = 0.0

# p1 = Product("A1", "Notebook")
# p2 = Product("B2", "Pencil", 1.5)

# print("sku: ", p1.sku, "name: ", p1.name, "price: ", p1.price)
# print("sku: ", p2.sku, "name: ", p2.name, "price: ", p2.price)

# Nested Dataclasses (Struct inside Struct)

# from dataclasses import dataclass

# @dataclass
# class Date:
#    day: int
#    month: int
#    year: int

# @dataclass
# class Employee:
#   empnum: int
#    name: str
#   birth: Date
#    height_cm: int|None = None

# create nested object
# e = Employee(9245, "Jony", Date(7, 5, 2000), 175)
# print("Employee Name: ", e.name)
# print("Day Employee was born: ", e.birth.day)
# print("Birth Month: ", e.birth.month)
# print("Year of Birth: ", e.birth.year)
# print("Height: ", e.height_cm)

# Student Honor Status

# from dataclasses import dataclass

# @dataclass
# class Student:
#    id: int
#    name: str
#    gpa: float = 0.0

#    def honor_status(self) -> str:
#        if self.gpa >= 3.5:
#            return "High Honor"
#        else:
#            return "Regular"

# s = Student(1, "Ali", 2.6)
# print("Student_ID: ", s.id)
# print("Student_Name: ", s.name)
# print("Honor Status: ", s.honor_status())

# Working with Collections Objects

# from dataclasses import dataclass

# @dataclass
# class Student:
#   id: int
#   name: str
#    gpa: float

# students = [
#    Student(1, "Ali", 3.2),
#    Student(2, "Ayse", 2.9),
#    Student(3, "Efe", 3.8),
# ]

# for st in students:
#    print(st.id, st.name, st.gpa)
#    print(students[0].name)

# Ordering in Dataclasses

# from dataclasses import dataclass

# @dataclass(order=True)
# class Grade:
#    Score: float
#    Student_id: int

# g1 = Grade(85.0, 101)
# g2 = Grade(92.5, 102)

# print(g1 < g2)
# print(g2 > g1)

# using index and range

# ages = [12, 18, 32, 19]

# for i in range(len(ages)):
#              print(f"Element is at index {i} = {ages[i]}")

# filling a list from user input and displaying

# n = int(input("How many number: "))

# number = []

# for i in range(n):
#        value = int(input(f"\n Enter Number {i+1}"))
#        number.append(value)
#        print("\n Enter Number are: ", number)

# age = [10, 20, 30, 40]

# print("Second Element is: ", age[2])

# age[3] = 35

# print("The updated list are: ", age)

age = 18

# for i in range(age):
if age >= 20:
    print("Your are Eligible for the Job Interview")

else:
    print("You are too Young for the Job Interview")
