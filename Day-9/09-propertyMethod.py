# examples of property method

# Getting the percentage of the marks. 
class Student():

  def __init__(self, phy, chem, math):
    self.phy = phy
    self.chem = chem
    self.math = math
    self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)            # Will print 86
print(stu1.percentage)     # Will print the old percentage value. % didnt get updated as per the new value.

# Method-1 How to get the updated percentage
class Student():

  def __init__(self, phy, chem, math):
    self.phy = phy
    self.chem = chem
    self.math = math
    #self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

  def percentage(self):
    self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)            # Will print 86
print(stu1.percentage)     # New % will be calculated

# Method-2 Better way to get the updtaed percentage using property decorator
class Student():

  def __init__(self, phy, chem, math):
    self.phy = phy
    self.chem = chem
    self.math = math

  @property
  def percentage(self):
    return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)            # Will print 86
print(stu1.percentage)     # New % will be updated.
