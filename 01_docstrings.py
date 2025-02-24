#The triple quotes symbolises the docstring written within the function 


class Calculator:
    """A simple calculator class to demonstrate docstrings."""

    def add(self, a, b):
        """Returns the sum of two numbers.

        Parameters:
        a (int or float): First number.
        b (int or float): Second number.

        Returns:
        int or float: Sum of a and b.
        """
        return a + b

    def multiply(self, a, b):
        """Returns the product of two numbers."""
        return a * b


# Example Usage
calc = Calculator()
print("Addition:", calc.add(3, 5))  # Output: 8
print("Multiplication:", calc.multiply(4, 6))  # Output: 24

# Accessing docstrings
print(calc.add.__doc__)

#After running this statement we will be able to see  what is written inside the function as comments 