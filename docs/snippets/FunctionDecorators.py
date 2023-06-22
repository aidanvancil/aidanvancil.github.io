# Decorator function without arguments
def decorator_function(func):
    def wrapper(*args, **kwargs):
        # Code to execute before the original function
        print("Decorator: Before function execution")
        # Call the original function
        result = func(*args, **kwargs)
        # Code to execute after the original function
        print("Decorator: After function execution")
        # Return the result of the original function
        return result
    return wrapper

# Decorator function with arguments
def decorator_function_with_arguments(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Code to execute before the original function
            print(f"Decorator: Before function execution with arguments {arg1} and {arg2}")
            # Call the original function
            result = func(*args, **kwargs)
            # Code to execute after the original function
            print("Decorator: After function execution")
            # Return the result of the original function
            return result
        return wrapper
    return decorator

# Class-based decorator
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Code to execute before the original function
        print("Decorator: Before function execution")
        # Call the original function
        result = self.func(*args, **kwargs)
        # Code to execute after the original function
        print("Decorator: After function execution")
        # Return the result of the original function
        return result

# Applying a decorator to a function
@decorator_function
def my_function():
    print("Original function")

# Applying a decorator with arguments to a function
@decorator_function_with_arguments("arg1_value", "arg2_value")
def my_function_with_arguments():
    print("Original function with arguments")

# Applying a class-based decorator to a function
@DecoratorClass
def my_function_class():
    print("Original function")

# Invoking decorated functions
my_function()
my_function_with_arguments()
my_function_class()
