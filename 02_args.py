#1.Args , which needs to be passed as a tuple using the * operator

class MathOperations:
    """Demonstrates the use of *args in OOP."""

    def sum_all(self, *args):
        """Returns the sum of all arguments.

        Parameters:
        *args (int or float): Variable number of numbers.

        Returns:
        int or float: Sum of all provided numbers.
        """
        return sum(args)


# Example Usage
math_ops = MathOperations()
print("Sum:", math_ops.sum_all(2, 4, 6, 8))  # Output: 20
print("Sum with more numbers:", math_ops.sum_all(1, 3, 5, 7, 9, 11))  # Output: 36
