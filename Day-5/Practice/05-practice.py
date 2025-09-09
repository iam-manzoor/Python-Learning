# Search for a number X in this tuple using loop

tup = (1,4,9,16,25,36,49,64,81,100)

search = int(input("Enter the number to search : "))
i = 0
found = False

while i < len(tup):
  if tup[1] == search:
    print(f"{search} found at the index {i}")
    found = True
    break
  i += 1

if not found:
  print(f"{search} not found in the list")
