# Inheritance Example.

class car():                  # Parent class
  
  color = "Black"
  
  @staticmethod
  def start():
    print("Car Started..")

  @statcimethod
  def stop():
    print("Car Stopped..")

class Toyata(car):              # Child class Inheritance to parent class

  def __init__(self,name):
    self.name = name

c1 = Toyata("Fortuner")
print(c1.name)

print(c1.start())                # Prints "Car Started..."
print(c1.color)
