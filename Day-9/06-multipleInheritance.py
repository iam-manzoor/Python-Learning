# Multiple Inheritance

class A:
  varA = "Welcom to class A"

class B:
  varB = "Welcom to class B"

class C(A,B):
  varC = "Welcom to class C"

c1 = c()

print(c1.varC)
print(c1.varB)
print(c1.varA)
