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
5. **class method**
   - A class method is bound to the class and not instance of the class.
   - It can access, modify class variables that are shared among all instances.
   - `class method` is a decorator.
   ```
   class Car():
     wheels = 4
     @classmethod
     def change_wheels(cls, num):
       cls.wheels = num

   print(Car.wheels)
   Car.change_wheels(6)
   print(Car.wheels)
   ```
       
6. **property decorator**
   - We use `@property` decorator on any method in the class to use the method as a property.
   - The phy values updated but the percentage doesnt change. Still showing the old percentage.

7. **Polymorphism : Operator Overloading**
   - When the same operator is alllowed to have different meaning according to the context. Polymorphism meaning different forms.
   - Every class such as `int` `list` `string` have different meaning for the operators. Based on the class the operator behaviour changes.
   - `implicit overloading` which means in python its already done. We can use the same concept in our classes.
   - `Dunder functions` functions that startes with double underscore `__add__` and ends with double underscore. 
   
