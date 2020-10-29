class Bankaccount:
  def __init__(self, int_rate, balance):
    self.interestRate = int_rate
    self.balance = balance

  def deposite(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    if self.balance < amount:
      print("Insufficient funds: Charging $5 fees")
      self.balance -=5
    else:
      self.balance -= amount
    return self

  def display_info(self):
    print(f"Balance: ${self.balance}")

  def yield_interest(self):
    if self.balance>0:
      self.balance = self.balance * self.interestRate + self.balance
    return self

account1 = Bankaccount(0.03, 100)
account2 = Bankaccount(0.1, 200)

account1.deposite(100).deposite(20).deposite(40).withdraw(10).yield_interest().display_info()

account2.deposite(200).deposite(300).withdraw(40).withdraw(10).withdraw(30).yield_interest().display_info()
