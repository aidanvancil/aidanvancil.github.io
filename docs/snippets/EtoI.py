# The examples for the `eval()` and `enumerate()` functions are included here.

# eval() - evaluates a string as a Python expression and returns the result
expression = "3 + 4 * 2"
result = eval(expression)
print(result)  # Output: 11

# enumerate() - returns an iterator of pairs containing the index and value of each element in an iterable
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# exec() - executes a dynamically created program represented as a string or code object
source_code = '''
def multiply(x, y):
    return x * y

result = multiply(3, 4)
print(result)
'''

exec(source_code)  # Output: 12

# The `exit()` function is typically used interactively in the Python shell to exit the interpreter.
# If executed in a script, it would terminate the script execution.
# Example usage:
# exit()

# filter() - constructs an iterator from elements of an iterable for which a function returns True
numbers = [1, 2, 3, 4, 5, 6]

# Example 1: Filtering even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# Example 2: Filtering numbers greater than 3
filtered_numbers = list(filter(lambda x: x > 3, numbers))
print(filtered_numbers)  # Output: [4, 5, 6]


# float() - returns a floating-point number from a number or string
num_str = "3.14"
num_float = float(num_str)
print(num_float)  # Output: 3.14


# format() - formats a value into a string using placeholders
name = "Alice"
age = 25
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)  # Output: My name is Alice and I am 25 years old.


# frozenset() - returns an immutable frozenset object
my_set = frozenset([1, 2, 3])
print(my_set)  # Output: frozenset({1, 2, 3})

# getattr() - returns the value of a named attribute of an object
class Person:
    name = "Alice"
    age = 25

person = Person()
name_value = getattr(person, "name")
print(name_value)  # Output: Alice


# globals() - returns a dictionary representing the current global symbol table
globals_dict = globals()
print(globals_dict)  # Output: {'__name__': '__main__', '__doc__': None, '__package__': None, ...}

# hasattr() - checks if an object has a given named attribute
class Rectangle:
    length = 5
    width = 3

rect = Rectangle()
has_length = hasattr(rect, "length")
has_height = hasattr(rect, "height")
print(has_length)  # Output: True
print(has_height)  # Output: False


# hash() - returns the hash value of an object
hash_value = hash("Hello")
print(hash_value)  # Output: 7021573631570088304


# help() - displays information about an object
help(list)
help(dict)


# hex() - converts an integer to a hexadecimal string
num = 255
hex_value = hex(num)
print(hex_value)  # Output: 0xff

# id() - returns the unique identifier of an object
my_list = [1, 2, 3]
list_id = id(my_list)
print(list_id)  # Output: <unique identifier>


# input() - reads user input from the console
name = input("Enter your name: ")
print("Hello, " + name)


# int() - converts a number or string to an integer
num_str = "10"
num_int = int(num_str)
print(num_int)  # Output: 10


# isinstance() - checks if an object is an instance of a class or a subclass thereof
class Person:
    pass

person = Person()
print(isinstance(person, Person))  # Output: True


# issubclass() - checks if a class is a subclass of another class
class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))  # Output: True


# iter() - returns an iterator object
my_list = [1, 2, 3]
iter_obj = iter(my_list)

print(next(iter_obj))  # Output: 1
print(next(iter_obj))  # Output: 2
print(next(iter_obj))  # Output: 3
