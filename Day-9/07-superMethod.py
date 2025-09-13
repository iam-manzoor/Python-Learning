# super() method example.

class car():                  # Parent class

  def __init__(self, type):
    self.type = type
    print(f"{self.type} is future")
  
  @staticmethod
  def start():
    print("Car Started..")

  @statcimethod
  def stop():
    print("Car Stopped..")

class Toyata(car):              # Child class Inheritance to parent class

  def __init__(self,name,type):
    super().__init__(type)
    self.name = name
    super().start()            # Calling start method from parent class

car1 = Toyata("Fortuner","electric")
print(car1.name)
car1.type
