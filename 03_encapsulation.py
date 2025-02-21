#Private attribute (__balance) ensures controlled access.
#Getter and Setter methods allow modification in a safe manner.


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute

    # Getter method to access private attribute
    def get_balance(self):
        return self.__balance

    # Setter method to modify private attribute
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount!")

# Creating an object
account = BankAccount("123456", 5000)

# Accessing public attribute
print("Account Number:", account.account_number)

# Accessing private attribute (Will fail)
# print(account.__balance)  # Uncommenting this will raise AttributeError

# Using getter method to access private data
print("Balance:", account.get_balance())

# Using setter method to update private data
account.set_balance(7000)
print("Updated Balance:", account.get_balance())
