
#3. Kwargs ( Key word arguments which represents a dictionary )

class UserProfile:
    """Demonstrates the use of **kwargs in OOP."""

    def __init__(self, **kwargs):
        """Stores user information using kwargs.

        Parameters:
        **kwargs: Variable keyword arguments representing user details.
        """
        self.details = kwargs

    def display_info(self):
        """Displays all user information."""
        for key, value in self.details.items():
            print(f"{key}: {value}")


# Example Usage
user = UserProfile(name="Alice", age=25, city="New York", profession="Engineer")
#Passing the parameters of the constructor in the form a dictionary which symbolizes the keyword arguments
user.display_info()
