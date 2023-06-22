import random

# Generate a random sample from a list without replacement
my_list = [1, 2, 3, 4, 5]
sample = random.sample(my_list, k)

# Generate a random sample from a range without replacement
sample = random.sample(range(start, stop), k)

# Generate a random sample from a population without replacement
population = [1, 2, 3, 4, 5]
sample = random.sample(population, k)

# Generate a random sample from a population with replacement
sample = random.choices(population, k=k)

# Generate a random sample from a string without replacement
my_string = "Hello, World!"
sample = random.sample(my_string, k)

# Shuffle a list in-place
random.shuffle(my_list)

# Select a random element from a list
random_element = random.choice(my_list)

# Select multiple random elements from a list
random_elements = random.choices(my_list, k)

# Generate a random float within a specified range
random_float = random.uniform(start, stop)

# Generate a random integer within a specified range
random_integer = random.randint(start, stop)

# Generate a random boolean value (True or False)
random_boolean = random.choice([True, False])
