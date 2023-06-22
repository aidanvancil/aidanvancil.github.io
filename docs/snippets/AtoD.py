# abs() - returns the absolute value of a number
num = -10
abs_num = abs(num)
print(abs_num)  # Output: 10

# all() - returns True if all elements in an iterable are True
iterable1 = [True, True, True]
iterable2 = [True, False, True]
print(all(iterable1))  # Output: True
print(all(iterable2))  # Output: False

# any() - returns True if any element in an iterable is True
iterable3 = [False, False, False]
iterable4 = [False, True, False]
print(any(iterable3))  # Output: False
print(any(iterable4))  # Output: True

# ascii() - returns a string containing a printable representation of an object
obj = 'äöü'
ascii_str = ascii(obj)
print(ascii_str)  # Output: '\xe4\xf6\xfc'

# bin() - converts an integer to a binary string
num = 10
binary_str = bin(num)
print(binary_str)  # Output: '0b1010'

# bool() - converts a value to a Boolean (True or False)
value1 = 0
value2 = "Hello"
print(bool(value1))  # Output: False
print(bool(value2))  # Output: True

# bytearray() - returns a new array of bytes
arr = bytearray(b"Hello")
print(arr)  # Output: bytearray(b'Hello')

# bytes() - returns a new bytes object
bytes_obj = bytes([72, 101, 108, 108, 111])
print(bytes_obj)  # Output: b'Hello'

# callable() - checks if an object is callable
def my_func():
    pass

print(callable(my_func))  # Output: True

# chr() - returns a string representing a character
char = chr(65)
print(char)  # Output: 'A'

# classmethod() - converts a method into a class method
class MyClass:
    data = 10

    @classmethod
    def my_method(cls):
        return cls.data

result = MyClass.my_method()
print(result)  # Output: 10

# compile() - compiles a source into a code or AST object
source = "print('Hello, World!')"
code = compile(source, "<string>", "exec")
exec(code)  # Output: Hello, World!

# complex() - creates a complex number from real and imaginary parts
real_part = 3
imaginary_part = 4
complex_num = complex(real_part, imaginary_part)
print(complex_num)  # Output: (3+4j)

# delattr() - deletes an attribute from an object
class Person:
    name = "Alice"
    age = 25

person = Person()
print(person.name)  # Output: Alice
delattr(person, "name")
print(person.name)  # Raises an AttributeError

# dict() - creates a new dictionary or converts an iterable into a dictionary
empty_dict = dict()
print(empty_dict)  # Output: {}

iterable = [('a', 1), ('b', 2), ('c', 3)]
converted_dict = dict(iterable)
print(converted_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# dir() - returns a list of valid attributes for an object or the current module
dir_list = dir()
print(dir_list)  # Output: ['__builtins__', '__doc__', '__name__', ...]

class MyClass:
    def __dir__(self):
        return ['attr1', 'attr2']

obj = MyClass()
attr_list = dir(obj)
print(attr_list)  # Output: ['attr1', 'attr2']

# divmod() - returns the quotient and remainder of two numbers
result = divmod(10, 3)
print(result)  # Output: (3, 1)

# The example for the `del` statement is included here:
# del - deletes an object or a named attribute
my_list = [1, 2, 3]
del my_list[0]
print(my_list)  # Output: [2, 3]

class MyClass:
    name = "Alice"
    age = 25

del MyClass.age
print(MyClass.__dict__)  # Output: {'name': 'Alice', '__module__': '__main__', ...}
