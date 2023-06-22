# vars() - returns the __dict__ attribute of an object or a module
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(vars(person))  # Output: {'name': 'Alice', 'age': 25}

# zip() - returns an iterator that combines multiple iterables into tuples
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
zipped = zip(numbers, letters)
print(list(zipped))  # Output: [(1, 'A'), (2, 'B'), (3, 'C')]

# __import__() - dynamically imports a module
math_module = __import__('math')
print(math_module.pi)  # Output: 3.141592653589793
