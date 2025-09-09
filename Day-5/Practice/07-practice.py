# Search the element from the tuple 

tup = (1,4,9,16,25,36,49,64,81,100)
x = 49

idx = 0
for val in tup:
  if val == x:
    print(f"We found you {val} at the {idx} index")
    break
  idx += 1
    
