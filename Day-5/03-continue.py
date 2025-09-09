# continue statement example. This script prints only the odd numbers from the tuple, skipping even numbers using the continue statement.

num_lst = (1,4,9,16,25,36,49,64,81,100)
i = 0

while i < len(num_lst):
  if num_lst[i] %2 == 0:
    i += 1
    continue
  print(num_lst[i])
  i += 1
