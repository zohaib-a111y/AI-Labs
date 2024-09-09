# Using the print function to display a message on the console
print("----Simple print statement----\nProgramming makes life easier!!!\n")

# Getting user input and displaying it
# Note: The input function always returns a string
print("----Using input/output functions----")
user_input = input("Enter any string: ")
print(user_input)

# Demonstrating indentation
x = 1
if x > 0:
    print("----Demonstrating indentation----\nInside if condition")

# Data types in Python
print("\n----Various Data Types----")
a = 12
print(f"{a} is of type {type(a)}")
b = -12
print(f"{b} is of type {type(b)}")
c = 2.2
print(f"{c} is of type {type(c)}")
d = -2.2
print(f"{d} is of type {type(d)}")
st = "Strings"
print(f"{st} is of type {type(st)}")
com = complex(7, 7)
print(f"{com} is of type {type(com)}")
bol = True
print(f"{bol} is of type {type(bol)}")

# Special characters and escape sequences
print("\n---Special Characters and Escape Sequences---")
print("\\ represents a backslash.")
print("\'\t\' represents a tab.")
print("\'Python is an interpretable language.\' uses single quotes.")
print("\"Python is an interpretable language.\" uses double quotes.")

# Accessing string elements
print("\n----Accessing String Elements----")
s = "Simplicity is the only beauty."
print(s)
length = len(s)
print(f"Enter a number between 1 and {length} to display a character from the string: ")
num = int(input())
print(f"Requested character: {s[num-1]}")

# String slicing and methods
print("\n----String Slicing and Methods----")
slice_s = s[1:7]
print(slice_s)
# Using the replace method
print(s.replace('the', 'a'))
# Using the upper method
print(s.upper())
# Using the startswith method to check the starting character
print(s.startswith("S"))

# Lists in Python
print("\n----Lists in Python----")
languages = ['C#', 'Dart', 'Kotlin', 'Java']
print(languages)
numbers = [2, 4, 6, 8, 10]
print(numbers)
mixed_list = ['app', 7, 2.2]
print(mixed_list)

# List slicing
print("\n----List Slicing----")
slice_num = numbers[1:4]
print(slice_num)

# Arithmetic operators (+, -, *, /, **, %)
# Casting input to integer for arithmetic operations
print("\n----Arithmetic Operators----")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} % {num2} = {num1 % num2}")

# Conditional operators (and, or, not)
# Using if-else conditions
print("\n----Conditional Operators----")
age = int(input("Enter your age: "))
if age % 2 == 0 and age < 18:
    print(f"{age} is even and under 18")
elif age % 2 != 0 and age < 18:
    print(f"{age} is odd and under 18")
elif age % 2 == 0 and age > 18:
    print(f"{age} is even and above 18")
elif age % 2 != 0 and age > 18:
    print(f"{age} is odd and above 18")
else:
    print(f"{age} is even and equal to 18")

# Comparison operators
# Casting input to integer for comparison operations
print("\n----Comparison Operators----")
month = int(input("Enter your birth month (1-12): "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month entered!")

# Using >= operator with if-else conditions
# Casting input to integer for comparison
marks = int(input("Enter your marks in AI: "))
if marks >= 85:
    print("Your grade is A+")
elif marks >= 80:
    print("Your grade is A")
elif marks >= 75:
    print("Your grade is B+")
elif marks >= 71:
    print("Your grade is B")
elif marks >= 68:
    print("Your grade is B-")
elif marks >= 64:
    print("Your grade is C+")
elif marks >= 61:
    print("Your grade is C")
elif marks >= 58:
    print("Your grade is C-")
elif marks >= 54:
    print("Your grade is D+")
elif marks >= 50:
    print("Your grade is D")
else:
    print("Your grade is F")
