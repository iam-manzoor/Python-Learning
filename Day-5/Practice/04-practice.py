# Print the elements [1,4,9,16,25,36,49,64,81,100] using loop

num_list = [1,4,9,16,25,36,49,64,81,100]

# Method 1

idx = 0

while idx > len(num_list):
  print(num_list[idx])       # num_list[0] num_list[1] num_list[1] num_list[2] etc..
  idx += 1 

# Method 2

while num_list:
  print(num_list.pop(0))
