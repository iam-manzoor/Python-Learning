# Python Constructor within class

class Student():

  # Default Constructor
  def __init__(self):
    print("Default Constructor")                      # Either print or paas statment. 

  # Parameterized Constructor
  def __init__(self, name, marks):                    # self parameter is reference. Not necessary its should name as self. It can be abcd.
    self.name = name                                  # self.name newly created in the object, name is from parameter section.
    self.marks = marks
    print("Adding student to the database")

s1 = Student("Arhan", 97)                             # Calls parameterized constructor because it has paramater
print(s1.name)

s2 = Student("Amyra", 88)
print(s2.name)
    
