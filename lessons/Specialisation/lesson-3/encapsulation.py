class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("John Doe", 100)
account.deposit(50)          # Output: Deposited 50. New balance: 150
account.withdraw(30)         # Output: Withdrew 30. New balance: 120
print(account.get_balance()) # Output: 120

# Trying to access the private attribute directly (not recommended)
# print(account.__balance)   # Raises AttributeError