# Class to get student name and print the avarage.

class Student():

  def __init__(self,name,marks):
    self.name = name
    self.marks =marks

  def cal_avg(self):
    return sum(self.marks)/len(self.marks)

s1 = Student("Arhan",[95,98,99])
print(self.name)
print(self.marks)

print(s1.cal_avg())
