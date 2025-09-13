# Attributes as private

class Account():

 def __init__(self,acc_number,acc_pass):
   self.acc_number = acc_number
   self.__acc_pass = acc_pass

cus = Account(1234,1000)

print(cus.acc_number)
print(cus.acc_pass)     # Will print the class Account has no attribut acc_paas
print(cus.__acc_pass)   # Will print the class Account has no attribut __acc_paas
