# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values
print(my_dict['name'])  # Output: John
print(my_dict.get('age'))  # Output: 30

# Modifying values
my_dict['age'] = 35
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York'}

# Adding new key-value pairs
my_dict['country'] = 'USA'
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York', 'country': 'USA'}

# Removing key-value pairs
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'country': 'USA'}

# Checking if a key exists
if 'name' in my_dict:
    print('Key exists')

# Iterating over keys
for key in my_dict:
    print(key)  # Output: name, age, country

# Iterating over values
for value in my_dict.values():
    print(value)  # Output: John, 35, USA

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)  # Output: name John, age 35, country USA

# Getting the number of key-value pairs
print(len(my_dict))  # Output: 3

# Clearing all key-value pairs
my_dict.clear()
print(my_dict)  # Output: {}
