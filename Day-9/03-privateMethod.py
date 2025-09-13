# Private Method definition.

class Person():
  __name = anonymous         # Private attribut

  def __hello(self):         # Private method.
    print("Hello Person")

  def welcome(self):
    self.__hello()

p1 = Person()

p1.welcome()

p1.__hello()                 # Will throw an error.
