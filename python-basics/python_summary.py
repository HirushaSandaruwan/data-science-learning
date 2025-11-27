# python_basics_summary.py

# Variables and Data Types
age = 21  # Age of a person
name = "John"  # Name of a person
full_name = name + " Doe"  # Concatenate name with surname
print(f"Full Name: {full_name}, Age: {age}")

# Receiving Input
user_name = input("Enter your name: ")  # Get user's name as input
print(f"Hello, {user_name}!")  # Display a greeting with user's name

# Type Conversion
height_in_meters = "1.75"  # height as a string
height_in_float = float(height_in_meters)  # Convert string to float
print(f"Height in meters: {height_in_float}")

# Arithmetic Operations
num1 = 15
num2 = 4
# Performing basic arithmetic operations and printing results
print(f"Addition: {num1 + num2}, Subtraction: {num1 - num2}, Multiplication: {num1 * num2}")

# Strings and String Methods
quote = "   Python is amazing!   "
print(quote.strip())  # Remove leading and trailing whitespace
print(quote.lower())  # Convert the string to lowercase

# If Statements
temperature = 30
# Conditional check for temperature
if temperature > 25:
    print("It's hot outside!")
else:
    print("The weather is fine.")

# Loops: For and While
for i in range(3):
    print(f"Number {i} in for loop")  # Print numbers from 0 to 2

counter = 0
while counter < 3:
    print(f"Counter is {counter} in while loop")  # Loop until counter is 3
    counter += 1

# Nested Loops
for i in range(2):
    for j in range(2):
        print(f"Outer loop {i}, Inner loop {j}")  # Print combinations of outer and inner loop

# Lists and Tuples
fruits = ["apple", "banana", "orange"]
fruits.append("grapes")  # Add a new fruit to the list
print(fruits)

# Tuple: Immutable collection of items
coordinates = (10, 20)  # Tuple to store coordinates (x, y)
print(coordinates)

# Dictionaries
person = {"name": "John", "age": 21}  # Dictionary to store key-value pairs
print(person["name"])  # Access value by key
print(person.get("age"))  # Get age from dictionary using .get()

# Error Handling (Try-Except)
try:
    num = int(input("Enter a number: "))  # Try to convert input to integer
    print(f"Your number is {num}")
except ValueError:
    print("Oops! That was not a valid number.")

# List Comprehensions
squares = [x ** 2 for x in range(5)]  # List of squares of numbers from 0 to 4
print(squares)

# Modules and Imports
import math  # Importing the math module
print(math.sqrt(16))  # Using sqrt() from the math module

# File Handling
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Reading from a file
with open("example.txt", "r") as file:
    print(file.read())

# Functions
def greet_user(username):
    """Function to greet the user by their username"""
    return f"Hello, {username}!"

print(greet_user("Alice"))  # Call the function with "Alice" as argument

# Simple Project: Weight Converter
def weight_converter(weight, unit):
    """Converts weight between kilograms and pounds"""
    if unit == "kg":
        return weight * 2.20462  # Convert kg to pounds
    elif unit == "lbs":
        return weight * 0.453592  # Convert pounds to kg
    else:
        return "Invalid unit"

print(weight_converter(70, "kg"))  # Convert 70 kg to pounds

