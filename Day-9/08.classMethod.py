# Class method example

# cant change the class attribute
class Person:
  name = "anonymous"

  def change_name(self,name):   # Instance Method
    self.name = name            # Creats the name var inside the instance, different from class var name

p1 = person()
p1.change_name("Arhan")
print(p1.name)                  # prints Arhan
print(Person.name)              # Prints anonymous

# Method-1 to change the class attribut
class Person:
  name = "anonymous"

  def change_name(self,name):
    Person.name = name            # Updates the class attribute. class name

p1 = person()
p1.change_name("Arhan")
print(p1.name)                    # prints Arhan
print(Person.name)                # Prints Arhan

# Method-2 change the class attribut
class Person:
  name = "anonymous"

  def change_name(self,name):
    self.__class__.name = name  # Creats the name var inside the instance, different from class var name
    
p1 = person()
p1.change_name("Arhan")
print(p1.name)                  # prints Arhan
print(Person.name)              # Prints Arhan

# Method-3 using class method
class Person:
  name = "anonymous"
  
  @classmethod
  def change_name(cls,name):   # class method.
    cls.name = name            # Creats the name var inside the instance, different from class var name

p1 = person()
p1.change_name("Arhan")
print(p1.name)                  # prints Arhan
print(Person.name)              # Prints anonymous
