# Class to get student name and print the avarage.

class Student():

  def __init__(self,name,marks):
    self.name = name
    self.marks =marks

  def cal_avg(self):
    return sum(self.marks)/len(self.marks)

  # Method 2
  def get_avg(self):
    sum = 0
    for i in self.marks:
      sum += i
    print(f"Hi {self.name} your avg score is {sum / len(self.marks)}")

s1 = Student("Arhan",[95,98,99])
print(self.name)
print(self.marks)

# Name overwrite
s1.name = "Manzoor"

print(s1.name)                  # Prints the name Manzoor. Overwrite the existing value
print(s1.cal_avg())
print(Student.cal_avg(s1))      # Same as above

