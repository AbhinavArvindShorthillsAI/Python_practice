#1. Local Scope 
class LocalScope:
    def local_example(self):
        x = 5  # Local variable
        print("Inside function, x:", x)  # Output: Inside function, x: 5

example = LocalScope()
example.local_example()
print(x)  
# Would raise an error because x is not defined globally


#2.Non local scope 
class NonLocalIntegerExample:
    def outer_function(self):
        count = 10  # Enclosing variable (integer)
        
        class InnerClass:
            def inner_function(self):
                nonlocal count  # Refers to the enclosing 'count' variable
                count += 5  # Modifies the enclosing variable
                print("Inside inner_function, count:", count)  # Output: 15
        
        inner_instance = InnerClass()
        inner_instance.inner_function()
        print("After modification in outer_function, count:", count)  # Output: 15

example = NonLocalIntegerExample()
example.outer_function()
