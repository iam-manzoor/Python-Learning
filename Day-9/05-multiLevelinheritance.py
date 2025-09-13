# MultiLevelInheritance.
class car():                  # Parent class
  
  color = "Black"
  
  @staticmethod
  def start():
    print("Car Started..")

  @statcimethod
  def stop():
    print("Car Stopped..")

class Toyata(car):              # Child class Inheritance to parent class

  def __init__(self,brand):
    self.brand = brand

class Fortuner(Toyata):

  def __init__(self,type):
    self.type = type
  

c1 = Fortuner("disel")
print(c1.type)

print(c1.start())                # Prints "Car Started..."
print(c1.color)
