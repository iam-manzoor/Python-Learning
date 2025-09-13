# bank account function debit, credit and balance

class Account():

  def __init__(self,acc_number,acc_balance):
    self.acc_number = acc_number
    self.acc_balance = acc_balance

  def debit(self): # we also have parameter def debit(self,amount):
    deduct_amount = int(input("Enter the amount to be debited : "))
    if deduct_amount <= self.acc_balance:
      self-acc_balance -= deduct_amount
      print(f"{deduct_amount} is deducted")
    else:
      print("You dont have enough balance")
    self.print_balance()

  def credit(self):
    credit_amount = int(input("Enter the amount to be credited : "))
    if credit_amount > 0:
      self.acc_balance += credit_amount
    print(f"{credit_amount} is credited")
    self.print_balance()

  def print_balance(self):
    print(f"{self.acc_balance} is remaining in your account")

cus = Account(1234,1000)

cus.debit()
cus.credit()
#cus.print_balance()
    
