# Area and Perimeter of the circle

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return (22/7) * self.radius ** 2

  def perimeter(self):
    return 2 * (22/7) * self.radius


num1 = Circle(4)
print(num1.area())
print(num1.perimeter())

