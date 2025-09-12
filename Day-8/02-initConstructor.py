# Python Constructor within class

class Student():
  def __init__(self, fullname):                # self parameter is reference. Not necessary its should name as self. It can be abcd.
    self.name = fullname
    print("Adding student to the database")

s1 = Student("Arhan")
print(s1.name)

s2 = Student("Amyra")
print(s2.name)
    
