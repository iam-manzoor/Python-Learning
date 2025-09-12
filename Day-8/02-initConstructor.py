# Python Constructor within class

class Student():

  college_name = "Bharathiar University"              # class attribute
  name = "anonymous"                                  # obj.attr takes precedence if the same name defined in the class attribute.

  # Default Constructor
  def __init__(self):
    print("Default Constructor")                      # Either print or paas statment. 

  # Parameterized Constructor
  def __init__(self, name, marks):                    # self parameter is reference. Not necessary its should name as self. It can be abcd.
    self.name = name                                  # self.name newly created in the object, name is from parameter section.
    self.marks = marks                                # object attribute
    print("Adding student to the database")

s1 = Student("Arhan", 97)                             # Calls parameterized constructor because it has paramater
print(s1.name)
print(s1.college_name)

s2 = Student("Amyra", 88)
print(s2.name)
print(Student.college_name)
    
