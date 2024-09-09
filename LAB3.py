# Question no 1
# Numbers divisible by 7 and multiple of 5, between 1500 and 2700
i = 1500
for i in range(i, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

# Question no 2
# Temperature conversion between Fahrenheit and Celsius based on user choice
choice = int(input("Enter 1 to convert Fahrenheit to Celsius or Enter 2 to convert Celsius to Fahrenheit: "))
if choice == 1:
    fah = int(input("Enter temperature in Fahrenheit: "))
    cel = 5 * (fah - 32) / 9
    print("Temperature in Celsius: ", int(cel))
elif choice == 2:
    cel = int(input("Enter temperature in Celsius: "))
    fah = 9 * cel / 5 + 32
    print("Temperature in Fahrenheit: ", fah)
else:
    print("Invalid Choice!!!")

# Question no 3
# Number guessing game
import random
num = random.randint(1, 9)
i = True
while i:
    guess = int(input("Guess any number between 1 to 9: "))
    if num == guess:
        print("Well guessed!")
        i = False
    else:
        print("Try again!!!\n")

# Question no 4
# Pattern printing
star = 6
for i in range(star):
    for j in range(i):
        print("*", end="")
    print()
star = 4
for i in range(star):
    for j in range(star - i):
        print("*", end="")
    print()

# Question no 5
# Reverse a word
word = input("Enter a word: ")
length = len(word) - 1
for i in range(len(word)):
    print(word[length], end="")
    length -= 1
print()

# Question no 6
# Count even and odd numbers in a tuple
user_input = input("Enter space-separated integers (like 20 3 18): ")
my_tuple = tuple(int(item) for item in user_input.split())
even = 0
odd = 0
for i in my_tuple:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even numbers: ", even, " Number of odd numbers: ", odd)

# Question no 7
# Append elements to a list and print their types
my_list = []
no = int(input("Enter the number of elements you want to enter in the list: "))
for i in range(no):
    value = input("Enter element: ")
    my_list.append(value)

for i in my_list:
    print(i, " ", type(i))

# Question no 8
# Print numbers except 3 and 6
for x in range(7):
    if x == 3 or x == 6:
        continue
    print(x, end=" ")
print()

# Question no 9
# Fibonacci series up to 50
num1 = 1
num2 = 1
total = 0
print(num1, num2, end=" ")
while True:
    total = num1 + num2
    if total > 50:
        break
    print(total, end=" ")
    num1 = num2
    num2 = total
print()

# FizzBuzz program
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Question no 10
# Create and print a 2D array
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
arr = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        arr[i][j] = i * j

for i in range(m):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()

# Question no 11
# Convert input to lowercase
line = input("Enter sequence of lines (press Enter to terminate): ")
print(line.lower())

# Question no 12
# Validate binary numbers and print those divisible by 5
my_list = []
while True:
    num = input("Enter a four-digit binary number: ")
    my_list.append(num)
    choice = int(input("Enter 1 to add more numbers or 2 to terminate: "))
    if choice == 2:
        break

for binary in my_list:
    decimalNumber = int(binary, 2)
    if decimalNumber % 5 == 0:
        print(binary, end=" ")
print()

# Question no 13
# Count digits and letters in a string
user_string = input("Enter any string: ")
digit = 0
letter = 0
for char in user_string:
    if char.isdigit():
        digit += 1
    elif char.isalpha():
        letter += 1
print(f"Letters: {letter}\nDigits: {digit}")

# Question no 14
# Validate password based on given criteria
password = input("Enter your password (must contain at least 1 letter between [a-z], 1 letter between [A-Z], 1 number between [0-9], 1 character from [$#@], and be 6-16 characters long): ")
print()
password_length = len(password)
small_letter = 0
capital_letter = 0
digit = 0
special_letter = 0
if 6 <= password_length <= 16:
    for char in password:
        if 'a' <= char <= 'z':
            small_letter += 1
        elif 'A' <= char <= 'Z':
            capital_letter += 1
        elif '0' <= char <= '9':
            digit += 1
        elif char in "$#@":
            special_letter += 1
        else:
            print(f"{char} is an invalid character!")
else:
    print("Length should be between [6-16]")
    digit += 1

if small_letter == 0:
    print("Password must contain at least 1 letter between [a-z]")
if capital_letter == 0:
    print("Password must contain at least 1 letter between [A-Z]")
if digit == 0:
    print("Password must contain at least 1 digit between [0-9]")
if special_letter == 0:
    print("Password must contain at least 1 character from [$#@]")
if small_letter != 0 and capital_letter != 0 and digit != 0 and special_letter != 0:
    print("Valid password")
