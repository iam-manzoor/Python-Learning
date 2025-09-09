# for Loop example

# for Loop to traverse through list 

lst = [1,2,3,4,5]

for val in lst:
  print(val)

# for Loop to traverse through tuple

tup = (1,2,3,4,5)

for val in tup:
  print(val)

# for Loop traverse through string.

str ="iamArhan"

for val in str:
  print(val)

# Optional else in for loop
# else can be used in case if we are using break.

for val in str:
  if val == "n":
    print(f"{val} found")
    break
  print(val)
else:
  print("END")
# In the above for loop else will not get executed, because loop will break when it found the string "n"

