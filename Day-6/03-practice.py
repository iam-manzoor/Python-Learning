# Factorial function

def fact(n):
  mul = 1
  for i in range(n,0,-1):
    mul *= i
  print(f"Factorial of {n} is {mul}")

fact(5)
