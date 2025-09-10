# In this will see how the default arguments declared in functions.

# FUnction defined with out any default arguments

def cal_mul(a,b):
  print(a * b)
  return a * b

print(cal_mul(3,5))

# Functions with default argument

def cal_mul(a = 3,b = 6):
  print(a * b)
  return a * b

print(cal_mul())                     # Returns 18

# Declare default argument at the end in the parameters section

def cal_mul(a,b = 6):
  print(a * b)
  return a * b

print(cal_mul(3))                     # Returns 18


