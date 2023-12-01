user_string = input("Enter a string: ")
reversed_string = user_string[::-1]
print("Reversed string:", reversed_string)
num_1 = int(input("First number: "))
num_2 = int(input("Second number: "))
product_result = num_1 * num_2
print("The product is:", product_result)
x_input = input("Enter the value for x (true/false): ")
y_input = input("Enter the value for y (true/false): ")
x = x_input == "true"
y = y_input == "true"
if x and y:
    print("both are true")
elif not x and not y:
    print("both are false")
elif (x and not y) or (not x and y):
    print("one is true")
else:
    print("invalid input")
