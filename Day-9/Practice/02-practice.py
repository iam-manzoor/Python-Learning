class Employee:
  def __init__(self,role,department,salary):
    self.role = role
    self.department = department
    self.salary = salary

  def showDetails(self):
    print("role = ",self.role)
    print("Department = ", self.department)
    print("Salary = ", self.salary)

class Engineer(Employee):
  def __init__(self,name,age):
    self.name = name
    self.age = age
    super().__init__("Engineer","IT","75k")

engg1 = Engineer("Arhan","08")
engg1.showDetails()
