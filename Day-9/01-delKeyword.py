# Delete object and its properties. del keyword

class Student():

  def __init__(self, name):
    self.name = name

s1 = Student("Arhan")
print(s1.name)               # Prints the name
del s1.name                  # Delete the object property
print(s1.name)               # Throw an error

s2 = Student("Manzoor")
print(s2.name)
del s1                       # Delete the entire object.
