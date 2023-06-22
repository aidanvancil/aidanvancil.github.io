class MyClass:
    def my_method(self, x, y=None):
        if y is None:
            # Perform operation with only one parameter
            print("Performing operation with one parameter:", x)
        else:
            # Perform operation with two parameters
            print("Performing operation with two parameters:", x, y)

# Create an instance of MyClass
obj = MyClass()

# Call my_method with one parameter
obj.my_method(5)  # Output: Performing operation with one parameter: 5

# Call my_method with two parameters
obj.my_method(5, 10)  # Output: Performing operation with two parameters: 5 10


class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")

# Create instances of Shape and Circle
shape = Shape()
circle = Circle()

# Call the draw method on Shape instance
shape.draw()  # Output: Drawing shape

# Call the draw method on Circle instance
circle.draw()  # Output: Drawing circle
