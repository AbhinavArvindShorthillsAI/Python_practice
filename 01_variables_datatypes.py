class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def arithmetic_operations(self):
        print("Addition:", self.a + self.b)
        print("Subtraction:", self.a - self.b)
        print("Multiplication:", self.a * self.b)
        print("Division:", self.a / self.b)
        print("Modulus:", self.a % self.b)
        print("Exponentiation:", self.a ** self.b)
        print("Floor Division:", self.a // self.b)
    
    def comparison_operations(self):
        print("Equal:", self.a == self.b)
        print("Not Equal:", self.a != self.b)
        print("Greater Than:", self.a > self.b)
        print("Less Than:", self.a < self.b)
        print("Greater or Equal:", self.a >= self.b)
        print("Less or Equal:", self.a <= self.b)
    
    def bitwise_operations(self):
        print("Bitwise AND:", self.a & self.b)
        print("Bitwise OR:", self.a | self.b)
        print("Bitwise XOR:", self.a ^ self.b)
        print("Bitwise NOT (a):", ~self.a)
        print("Left Shift:", self.a << 2)
        print("Right Shift:", self.a >> 2)
    
    def logical_operations(self, x, y):
        print("Logical AND:", x and y)
        print("Logical OR:", x or y)
        print("Logical NOT:", not x)
    
    def assignment_operations(self):
        self.a += 5
        print("Updated a (after += 5):", self.a)


# Demonstrating Variable Types
class VariableDemo:
    def __init__(self):
        self.x = 10         # Integer
        self.y = "Hello"    # String
        self.z = 3.14       # Float
        self.a = True       # Boolean
    
    def display_variables(self):
        print(self.x, self.y, self.z, self.a)
        print("Type of x:", type(self.x))
        print("Type of y:", type(self.y))
        print("Type of z:", type(self.z))
        print("Type of a:", type(self.a))


# Execution
if __name__ == "__main__":
    print("Variable Demonstration:")
    var_demo = VariableDemo()
    var_demo.display_variables()
    
    print("\nCalculator Operations:")
    calc = Calculator(10, 5)
    calc.arithmetic_operations()
    calc.comparison_operations()
    calc.bitwise_operations()
    calc.logical_operations(True, False)
    calc.assignment_operations()









