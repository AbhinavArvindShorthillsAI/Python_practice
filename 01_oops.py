# Defining a class named 'Car'
class Car:
    # Constructor (__init__ method) to initialize object attributes
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute
        self.year = year  # Instance attribute

    # Method to display car details
    def display_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year})")

# Creating an object of the Car class
my_car = Car("Toyota", "Camry", 2023)

# Accessing attributes and methods
print(my_car.brand)  # Output: Toyota
my_car.display_info()  # Output: Car: Toyota Camry (2023)



#(ii) Deleting objects , and seeing the object details 


# Listing all attributes and methods of the object
print(my_car.__dir__())  # Outputs all available methods & attributes

# Deleting the object
del my_car

# Trying to access it now will raise an error
# print(my_car.brand)  # Uncommenting this will raise: NameError: name 'my_car' is not defined




