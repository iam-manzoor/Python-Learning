# Function that calls itself

# Print the unmbers in reverse order using recursion

def rev_num(n):
  if num == 0:
    return
  print(n)
  rev_num(n-1)

rev_num(6)

# Factorial using recursion

def fact(n):
  if n == 0  or n == 1:
    return 1
  return fact(n-1) * n

print(fact(5))
  
