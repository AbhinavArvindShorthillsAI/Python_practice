#1 Abstraction
#When you use an ATM, 
#you only press buttons to deposit/withdraw money. 
#You don’t see the backend transactions happening inside the bank's system.
class ATM:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (Cannot be accessed directly)

    # Public method to deposit money (User can use this)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    # Public method to withdraw money (User can use this)
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance!")

    # Private method (Hidden from the user)
    def __internal_bank_operations(self):
        print("Performing internal bank transactions...")

# Creating an ATM object
my_atm = ATM(5000)

# User interacts with deposit and withdraw (Public methods)
my_atm.deposit(1000)
my_atm.withdraw(2000)

# User cannot access private attributes/methods directly
# print(my_atm.__balance)  # Uncommenting this will raise AttributeError
# my_atm.__internal_bank_operations()  # Uncommenting this will raise AttributeError
