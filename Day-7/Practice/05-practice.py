# Find the count of the even number from the file. The numbers are comma seperated.

with open("numbers.txt", "r") as f:
  data = f.read()
  count = 0
  for i in data.split(","):  # split function converts it in to listbased on the split parameter
    i = int(i)
    if i % 2 == 0:
      count += 1
  print("Count of even numbers: ", count)
