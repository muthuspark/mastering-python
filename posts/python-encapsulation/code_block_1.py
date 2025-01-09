class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Convention indicating protected attribute

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

my_account = BankAccount(1000)
print(my_account.get_balance())  # Accessing balance through getter
my_account.deposit(500)
my_account.withdraw(200)
print(my_account.get_balance())
