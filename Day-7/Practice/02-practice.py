# Script to replace a string 

with open("practice.txt", "r") as f:
  data = f.read()
  
new_data = data.replace("java", "python")

with open("practice.txt", "r") as f:
  f.write(new_data)
