# Inheritance Example.

class car():                  # Parent class

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

print(c.start())                # Prints "Car Started..."
