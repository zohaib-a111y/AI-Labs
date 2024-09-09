# --------while loop 
print("\n----While Loop----")
count = 0
while count < 3:
    count += 1
    print("Hello Geek")
print()

# While loop practice by printing a multiplication table
num = int(input("Enter the number for which you want the multiplication table: "))
i = 1
while i < 11:
    print(f"{i} * {num} = {i * num}")
    i += 1

# -------for loop
print("\n----For Loop Traversal using List----")
ai = ['robotics', 'deep learning', 'automation']
for item in ai:
    print(item)
print()

print("\n----For Loop Traversal by Index of Sequence----")
li = ['windows', 'linux', 'macOS']
for index in range(len(li)):
    print(li[index])
print()

# For loop with break and continue statements
br = int(input("For loop will display numbers from 1 to 10. Enter the number at which you want to exit the loop (1-10): "))
for i in range(1, 11):
    print(i)
    if i == br:
        break
print()

con = int(input("Enter a number and the for loop will display only even numbers up to that number: "))
for i in range(1, con + 1):
    if i % 2 != 0:
        continue
    print(i)
print()

# ------function
print("\n-----Functions-----")
def display():  # Function declaration and initialization
    print("Programming makes life easy!!!")

display()  # Function call

# Function with parameters and return value
def sum(num1, num2):
    return num1 + num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Sum of {num1} + {num2} = {sum(num1, num2)}")

# Function with a keyword argument
name = input("Enter your name: ")
def greeting(name, message="have a nice day!!!"):
    print(f"{name}, {message}")
print()

greeting(name)

# Function to find factorial
def factorial(value):
    if value < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if value == 1 or value == 0:
        return 1
    return value * factorial(value - 1)

value = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {value} = {factorial(value)}")

# ---- class 
print("\n-----Class------")
class AI:
    description = "Classes are parts of Object Oriented Programming."

obj = AI()
print(obj.description)

# Class with __init__ method acting as constructor
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

na = input("Enter your name: ")
ag = int(input(f"Enter {na}'s age: "))
co = input(f"Enter {na}'s country: ")
p1 = Person(na, ag, co)
print(f"{p1.name} is {p1.age} years old and lives in {p1.country}.\n")

# Class with methods
# Create a Room class
class Room:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    # Method to calculate area
    def calculate_area(self):
        return self.length * self.breadth

# Create an object of Room class
length = float(input("Enter length of the room: "))
breadth = float(input("Enter breadth of the room: "))
study_room = Room(length, breadth)

# Access method inside class
print(f"Area of Room = {study_room.calculate_area()}")
