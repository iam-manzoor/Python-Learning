# Example of with

# with syntax read operation

with open("demo.txt", "r") as f:
  data = f.read()
  print(data)
  

# with syntax write operation

with open("demo.txt", "r") as f:
  f.write("New Data")
  
