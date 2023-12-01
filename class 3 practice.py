# if statements
x = 10
if x > 5: 
    print("x is greater than 5")
# elif
x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5: 
    print("x is 5")
# else
x = 3
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is 5")
else:
    print("x is not greater than 10 and x is not 5")
# example
x = 29
if x > 25:
    print("x is greater than 25")
elif x == 27:
    print("x is 27")
else:
    print("x is not greater than 25 and x is not 27")
# for loops
sports = ["golf", "football", "baseball", "hockey"]
for sport in sports:
    print(sport)
for i in range(8):
    print(i)
# while loop
count = 0
while count < 5:
    print(count)
    count += 1
# for loop with break
for i in range(10):
    if i == 5:
        break
    print(i)
# nested loops
for i in range(3):
    for j in range(2):
        print(i, j)
# even or odd number
number = int(input("enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
# multiplication table
num = int(input("Enter a number: "))
for i in range (1,6):
    print(f"{num} x {i} = {num*i}")
# chat gpt test 1
numbers = ["1", "2", "3", "4", "5"]
for num in numbers:
    print(num)
# chat gpt tst 2
for num in range(1, 5):
    square = num * num
    print(square)
# chat gpt test 3
colors = ["blue", "red", "green", "yellow"]
for color in colors:
    if color == "red":
        print("red")
    else:
        print("not red")
