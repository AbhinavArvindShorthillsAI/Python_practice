# Parent class
#Same function show_vehicle_info() works for both Car and Bike.
#Method Overriding (display_info()) changes the behavior for each class.
#super().display_info() calls the parent class method before adding extra information.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")
        

# Child class (inherits Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)  # Calls the constructor of Vehicle
        self.fuel_type = fuel_type  # Additional attribute for Car

    def display_info(self):  # Method Overriding
        super().display_info()  # Calls display_info() from Vehicle class
        print(f"Fuel Type: {self.fuel_type}")


# Child class (inherits Vehicle)
class Bike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc  # Additional attribute for Bike

    def display_info(self):  # Method Overriding
        super().display_info()  # Calls display_info() from Vehicle class
        print(f"Engine Capacity: {self.cc}cc")


# Function demonstrating polymorphism
def show_vehicle_info(vehicle):
    vehicle.display_info()  # Calls the respective method of Car or Bike

# Creating objects
car = Car("Toyota", "Corolla", "Petrol")
bike = Bike("Yamaha", "R15", 150)

# Using the same function to show different outputs (Polymorphism)
show_vehicle_info(car)
# Output:
# Vehicle: Toyota Corolla
# Fuel Type: Petrol

show_vehicle_info(bike)
# Output:
# Vehicle: Yamaha R15
# Engine Capacity: 150cc
