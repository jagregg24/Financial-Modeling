def add(a, b):
    """this function adds two numbers and returns their sum."""
    return a + b
result = add(12, 8)
print(result)
def greet(name, greeting):
    print(greeting, name)
greet("Alice", "Hello")
def add(*numbers):
    return sum(numbers)
print(add(9, 8, 7, 6))
def greet_user(name="User"):
    print(f"Hello, {name}!")
greet_user("Julia")
def introduce(first_name, last_name):
    print(f"My name is {first_name} {last_name}.")
introduce(first_name="Julia", last_name= "Gregg")
# max and min numbers
def min_max(nums):
    return min(nums), max(nums)
numbers = [9, 7, 5, 3, 1]
minimum, maximum = min_max(numbers)
print("Min:", minimum)
print("Max:", maximum)
# counts words in a sentence 
def word_count(s):
    words = s.split()
    return len(words)
sentence = "What is up how are you doing?"
print(word_count(sentence))
# area of a circle
import math
def circle_area(radius):
    return math.pi * (radius**2)
r =float(input("Enter the radius of the circle: "))
print(f"The area of the circle with radius {r} is:{circle_area(r)}")
#fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
n = int(input("Enter a value for n: "))
print(f"The {n}th Fibonacci number number is: {fibonacci(n)}")
def string_lengths(strings_list):
    return[len(s) for s in strings_list]
strings = ["apple", "banana", "cherry", "date"]
print(string_lengths(strings))
# test
def add(a, b):
    return a + b
result = add(5, 3)
print(result)
def greet(name="User"):
    return f"Hello, {name}!"
print(greet())
print(greet("Alice"))
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))