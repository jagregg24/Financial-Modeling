x = 5 #x is a type of int 
x = "john" 
print(x)
result = 5 + 3
print(result)
result = 6 * 4 
print(result)
bean = 4 % 200
print(bean)
a = 8
b = -a
print(b)
j = 8
f = 4
sum_result = j + f
product = j * f
division = j / f 
print(sum_result)
print(product)
print(division)
user_input = input("Enter your name: ")
print("Hello,", user_input, "!")

num1 =int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_result = num1+ num2
print("The sum is:", sum_result)
number_string = input("Enter a number: ")
# taking first number as input and converting to float
num1 = float(input("Enter the first number: "))
# second number as input and convert to float
num2 = float(input("Enter the second number: "))
# add them
sum_result = num1 + num2
# result
print("The sum is:", sum_result)
# area of a rectangle 
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area_result = length * width 
print("The area is:" , area_result)
# simple calculator example

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Undefined (division by zero)"
    else:
        return x / y

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose the operation
print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input()

# Perform the operation
if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid Input")

# celsius to fahrenheit
temp_c = float(input("Enter the temperature: "))
fahrenheit = (temp_c * 9/5) + 32
print(f"{temp_c} is equivalent to {fahrenheit}")

 # chatgpt ex
 # # Get input from user in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the formula
fahrenheit = (celsius * 9/5) + 32

# Display the result
print(f"{celsius}°C is equivalent to {fahrenheit}°F")
#input from the user and reversed
user_string = input("Enter a string: ")
reversed_string = user_string[::-1]
print("Reversed string:", reversed_string)
# booleans
x = True
y = False
print(x and y)
