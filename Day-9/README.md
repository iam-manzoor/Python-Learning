## Day 9 OOPS in python

1. **del keyword**
   - Used to delete object properties or object itself.
   - When you create an object its related methods and attributes are stored in the memory.
   - Delete object property/Attribute `del s1.name`
   - Delete complete object `del s1`
     
2. **Prinvate(like) attributes & methods**
   - Private attribute & methods are meant to be used only within the class and are not accessible from outside the class.
   - how to make an attribut private in python?
   ```
   class Account():

    def __init__(self,acc_number,acc_paas):
      self.acc_number = acc_number
      self.acc_balance = acc_balance

   cus = Account(1234,1000)

   print(cus.acc_number)
   print(cus.acc_pass)   # Will print the class Account has no attribut acc_paas
   print(cus.__acc_pass)   # Will print the class Account has no attribut __acc_paas
   ```
   - Inside class, a method can invoke another method which is private.
   ```
   class Person():
     __name = anonymous

     def __hello(self):         # Private method.
       print("Hello Person")

     def welcome(self):
       self.hello()

   p1 = Person()

   p1.welcome()
   ```
