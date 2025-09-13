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

    def __init__(self,acc_number,acc_pass):
      self.acc_number = acc_number
      self.__acc_balance = acc_pass

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
       self.__hello()

   p1 = Person()

   p1.welcome()
   ```

3. **Inheritance**
   - When one class derives properties & methods of another class is called inheritance.
     - Inheritance Types
       - Single Inheritance.  base class -> Derived class
       - Multi-level Inheritance. base class - > derived class -> derived class
       - Multiple Inheritance. more than one base class for the devived class.
      
4. **Super methods**
   - `super()` method is used to access methods of the parent class.
   ```
   super().__init__(type)  # From thebase class
   ```
