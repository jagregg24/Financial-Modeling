fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
print(fruits[0])
for fruit in fruits:
    print(fruit)
if "apple" in fruits:
    print("Apple is in the list!")
fruits = ("apple", "banana", "cherry")
a, b, c = fruits
print(a)
print(len(fruits))
repeat= (1, 1, 2, 2, 2, 2, 3, 4)
print(repeat.count(2))
dict1 = {'name': 'Julia', 'age': 22}
print(dict1["name"])
print(dict1.get('age'))
dict1['job'] = 'Student'
print(dict1['job'])
squares = {x: x*x for x in range(5)}
print(squares)
print(len(dict1))
def find_largest(nums):
    return max(nums)
numbers = [6, 5, 700, 48, 21, 56, 89, 546, 401]
largest_number = find_largest(numbers)
print(f"The largest number in the list is: {largest_number}")
def count_long_strings(strings):
    count = 0
    for s in strings:
        if len(s)>= 2:
            count += 1
    return count
string_list = ["a", "ab", "abc", "abcd", "x"]
result = count_long_strings(string_list)
print(f"Number of strings with length of 2 or more: {result}")
def remove_duplicates(input_list):
    return list(set(input_list))
original_list = [20, 20, 45, 50, 50, 50, 60, 1, 1, 1, 5, 5]
no_duplicates = remove_duplicates(original_list)
print("Original List", original_list)
print("List without duplicates:", no_duplicates)
def sum_of_tuple(numbers_tuple):
    return sum(numbers_tuple)
input_tuple = (50, 45, 1, 60, 800)
total_sum = sum_of_tuple(input_tuple)
print(f"Sum of the numbers in the tuple {input_tuple} is: {total_sum}")
def convert_to_dict(tuple_list):
    return dict(tuple_list)
tuple_list = [("a", 1), ("b", 2), ("c", 3)]
resulting_dict = convert_to_dict(tuple_list)
print(resulting_dict)
# test
def remove_duplicates(input_list):
    return list(set(input_list))
original_list = [20, 20, 45, 50, 50, 50, 60, 1, 1, 1, 5, 5]
no_duplicates = remove_duplicates(original_list)
print("Original List", original_list)
print("List without duplicates:", no_duplicates)
def remove_duplicates(input_list):
    output_list = []
    for i in input_list:
        if i not in output_list:
            output_list.append(i)
    return output_list
def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Example usage:
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = sum_of_even_numbers(numbers_tuple)
print(result)
def invert_dictionary(d):
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return {key: (val[0] if len(val) == 1 else val) for key, val in inverted.items()}

original_dict = {
    "a": 1,
    "b": 2,
    "c": 2,
    "d": 3
}
inverted_dict = invert_dictionary(original_dict)
print(inverted_dict)
