class InsufficientFundsError(Exception):
  pass

class Account:
  def __init__(self, balance):
    self.balance = balance

  def withdraw(self, amount):
    if self.balance < amount:
      raise InsufficientFundsError("Insufficient funds in the account.")
    self.balance -= amount
    print(f"Withdrawal successful. New balance: {self.balance}")

account = Account(100)
try:
  account.withdraw(150)
except InsufficientFundsError as e:
  print(f"Error: {e}")

account.withdraw(50)