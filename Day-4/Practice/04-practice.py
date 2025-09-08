
# Figure out a way to store 9 & 9.0 as seperate values in set. (Take help of built-in data types)

# Method 1
num = {9,"9.0"}

print(num)

# Method 2

num = {("int",9),("float",9.0)}

print(num)
