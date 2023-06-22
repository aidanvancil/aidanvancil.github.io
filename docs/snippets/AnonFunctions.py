# Create a lambda function
add = lambda x, y: x + y

# Call the lambda function
result = add(3, 4)  # Output: 7

# Use a lambda function as an argument
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

# Sort a list of tuples using a lambda function
students = [('Alice', 20), ('Bob', 18), ('Charlie', 22)]
students.sort(key=lambda student: student[1])

# Filter elements from a list using a lambda function
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Use a lambda function in a higher-order function
def apply_operation(numbers, operation):
    return [operation(x) for x in numbers]

squared_numbers = apply_operation(numbers, lambda x: x**2)

# Use multiple arguments with a lambda function
multiply = lambda x, y, z: x * y * z

# Store a lambda function in a variable
power = lambda base, exponent: base**exponent

# Create a recursive lambda function
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
