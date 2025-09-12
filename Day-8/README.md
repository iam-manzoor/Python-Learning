## Day-8 OOPS in Python

1. **OOP in Python**
   - To map with real world scenarios, we started using objects in code. This is called OOP.
   - What is Procedural Programming?
     - organize code into a sequence of instructions are called procedural programming.
   - What is function in Programming?
     -  Avoids redundancy and reusability.

2. **Class & Object in Python**
   - class is a blueprint for creating Object. Blueprint tells how the object should be created. Example addmission of a student. To get the student admitted we have to collect details such as his name, age, address, contact details, etc..
   - class name always starts with Capital character such as `Student`
   ```
   # Creating class
   class Student:
     name = "Arhan"
   ```
   ```
   # Creating Object (Instance) of the class
   s1 = Student()
   print(s1.name)
   ```

3. **__init__ Function**
   - Is a Constructor. All classes have a function called __init__(), which is always executed when the object is being initiated.
   - The function gets invoked when the object is created. `s1 = Student()` here s1 is the object.
   - When its not defined Python automatically invoke the function.
   - This function by default takes a one paramenter called `self` `def __init__(self)`.
   - `self` points to the object it invoked.
   - We can also pass multiple parameters. `def __init__(self, fullname)`.
   - The **self** parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
   - The data that is stored inside the class and objects is called **attributes**
   - We have default constructor and parameterized constructors.
  
4. **Class & Instance Attributes**
   - class attributes common to all the classes.
   - instance attribute unique to each object. And we refer it with `self.name`
   - object attribute takes precedence over the class attribute if they have the same var name.

5. **Methods**
   - Methods are functions that belong to objects. Function written inside the class is called method.
   - Class can store data and methods. Class is a collection of data and methods. Methods are like functions.
