class User:
  def __init__(self, nameInput, emailId, ageInput):
    self.totalBalance = 0
    self.name = nameInput
    self.emailid = emailId
    self.age = ageInput

  def make_deposite(self, bal):
    self.totalBalance += bal

  def make_withdrawal(self, bal):
    self.totalBalance -= bal

  def tansfer_money(self, amount, receiver):
    self.totalBalance -= amount
    receiver.totalBalance += amount

  def displayBalance(self):
    print(f"User Name: {self.name} Total Balance: {self.totalBalance}")

user1 = User ("Lisa", "lisa@gmail.com", 23)
user2 = User ("Rina", "rina123@gmail.com", 45)
user3 = User ("Smith", "ssoloway@gmail.com", 34)

user1.make_deposite(100)
user1.make_deposite(500)
user1.make_deposite(50)
user1.make_withdrawal(100)

user1.displayBalance()

user2.make_deposite(100)
user2.make_deposite(500)
user2.make_withdrawal(50)
user2.make_withdrawal(100)

user2.displayBalance()

user3.make_deposite(500)
user3.make_withdrawal(100)
user3.make_withdrawal(50)
user3.make_withdrawal(100)

user3.displayBalance()

user1.tansfer_money(10, user3)

user1.displayBalance()
user3.displayBalance()