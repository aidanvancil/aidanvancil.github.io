# object() - returns a new featureless object
my_object = object()
print(my_object)  # Output: <object object at 0x7fbf1a40f130>


# oct() - converts an integer to an octal string
decimal_number = 10
octal_number = oct(decimal_number)
print(octal_number)  # Output: 0o12


# open() - opens a file and returns a file object
file_path = "example.txt"
file_obj = open(file_path, "r")
content = file_obj.read()
print(content)
file_obj.close()


# ord() - returns the Unicode code point of a character
character = 'A'
unicode_value = ord(character)
print(unicode_value)  # Output: 65

# pow() - returns the value of x raised to the power of y
result = pow(2, 3)
print(result)  # Output: 8


# print() - prints objects to the text stream
name = "Alice"
age = 25
print("Name:", name, "Age:", age)  # Output: Name: Alice Age: 25


# property() - creates a property attribute for a class
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

person = Person("Alice")
print(person.name)  # Output: Alice

person.name = "Bob"
print(person.name)  # Output: Bob

# range() - returns a sequence of numbers from start to stop (exclusive) with a step size
numbers = list(range(1, 10, 2))
print(numbers)  # Output: [1, 3, 5, 7, 9]


# repr() - returns a string containing a printable representation of an object
name = "Alice"
representation = repr(name)
print(representation)  # Output: 'Alice'


# reversed() - returns a reverse iterator for a sequence
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)  # Output: [5, 4, 3, 2, 1]


# round() - rounds a number to the nearest integer or a specified number of decimals
pi = 3.14159
rounded_pi = round(pi, 2)
print(rounded_pi)  # Output: 3.14

# set() - creates a new set object
my_set = set([1, 2, 3, 3, 4, 5, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}


# setattr() - sets the value of an attribute on an object
class Person:
    pass

person = Person()
setattr(person, 'name', 'Alice')
print(person.name)  # Output: Alice


# slice() - creates a slice object that represents a range of indices
numbers = [1, 2, 3, 4, 5]
my_slice = slice(1, 4)
sliced_numbers = numbers[my_slice]
print(sliced_numbers)  # Output: [2, 3, 4]


# sorted() - returns a new sorted list from the elements of an iterable
numbers = [5, 2, 4, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5]


# staticmethod() - converts a method into a static method
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

result = MathUtils.add(2, 3)
print(result)  # Output: 5


# str() - converts an object into a string representation
my_number = 123
my_string = str(my_number)
print(my_string)  # Output: '123'


# sum() - returns the sum of all elements in an iterable
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # Output: 15


# super() - returns a temporary object of the superclass to call its methods
class Vehicle:
    def drive(self):
        print("Driving a vehicle")

class Car(Vehicle):
    def drive(self):
        super().drive()
        print("Driving a car")

car = Car()
car.drive()
# Output:
# Driving a vehicle
# Driving a car

# tuple() - creates a new tuple object
my_tuple = tuple([1, 2, 3, 4, 5])
print(my_tuple)  # Output: (1, 2, 3, 4, 5)


# type() - returns the type of an object
name = "Alice"
print(type(name))  # Output: <class 'str'>

number = 10
print(type(number))  # Output: <class 'int'>

my_list = [1, 2, 3]
print(type(my_list))  # Output: <class 'list'>
