# Print the multiplication table of a number n

num = int(input("Enter the multiplication table number : "))
idx = int(input("Enter range till the table to be printed : "))
mul = 1

while idx > 0:
  val = num * mul
  print(f"{num} X {mul} = {val}")
  idx -= 1
  mul += 1
