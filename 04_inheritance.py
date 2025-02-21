# Parent class
#The Dog class inherits from Animal, reusing attributes.
#super().__init__(name) calls the parent constructor, so name is not redefined.
#speak() is overridden, meaning Dog has a custom implementation.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("This animal makes a sound.")

# Child class (inherits Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls the constructor of the parent class
        self.breed = breed  # Additional attribute for Dog class

    def speak(self):  # Method Overriding
        print(f"{self.name} (a {self.breed}) says: Woof Woof!")

# Creating an object of Dog class
dog = Dog("Buddy", "Golden Retriever")

# Accessing inherited attribute
print("Dog's Name:", dog.name)  # Inherited from Animal class

# Calling overridden method
dog.speak()  # Output: Buddy (a Golden Retriever) says: Woof Woof!
