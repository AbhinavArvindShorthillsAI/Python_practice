#1.Global Scope 

x = 10  # Global variable

class Example:
    def show_global(self):
        print("Global x:", x)  # Accessing global variable

example = Example()
example.show_global()  # Output: Global x: 10




#2. Usage of global keyword 

# Accessing global variable inside a function
x = 20  # Global variable

class GlobalKeywordExample:
    def modify_global(self):
        global x  # Refers to the global x
        x = 50  # Modifies the global variable
        print("Inside function, modified global x:", x)

example = GlobalKeywordExample()
example.modify_global()
print("Outside function, global x:", x)  # Output: 50


