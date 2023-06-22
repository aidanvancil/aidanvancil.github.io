# len() - returns the length (number of elements) of an object
my_list = [1, 2, 3, 4, 5]
list_length = len(my_list)
print(list_length)  # Output: 5

my_string = "Hello, World!"
string_length = len(my_string)
print(string_length)  # Output: 13


# list() - creates a new list object or converts an iterable into a list
empty_list = list()
print(empty_list)  # Output: []

my_tuple = (1, 2, 3)
converted_list = list(my_tuple)
print(converted_list)  # Output: [1, 2, 3]


# locals() - returns a dictionary representing the current local symbol table
def example_function():
    message = "Hello, Python!"
    local_symbols = locals()
    print(local_symbols)

example_function()
# Output: {'message': 'Hello, Python!', 'local_symbols': {...}, ...}
# The output will contain additional local symbols defined in the current scope

# map() - applies a function to each element of an iterable
numbers = [1, 2, 3, 4, 5]

# Example 1: Square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 2: Convert numbers to strings
string_numbers = list(map(str, numbers))
print(string_numbers)  # Output: ['1', '2', '3', '4', '5']


# max() - returns the largest item from an iterable or the largest of two or more arguments
numbers = [5, 2, 8, 1, 9]
max_number = max(numbers)
print(max_number)  # Output: 9


# memoryview() - returns a memory view object of an object's memory
my_list = [1, 2, 3, 4, 5]
memory_view = memoryview(my_list)
print(memory_view)  # Output: <memory at 0x7fbf1a421340>


# min() - returns the smallest item from an iterable or the smallest of two or more arguments
numbers = [5, 2, 8, 1, 9]
min_number = min(numbers)
print(min_number)  # Output: 1


# next() - retrieves the next item from an iterator
numbers = iter([1, 2, 3])
print(next(numbers))  # Output: 1
print(next(numbers))  # Output: 2
print(next(numbers))  # Output: 3
