class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number #protected attribute
        self._balance = balance #protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
        return self._balance

account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Account balance: {account.get_balance()}")

#Trying to directly access the protected attributes will work, but it is discouraged
#print(account._balance)