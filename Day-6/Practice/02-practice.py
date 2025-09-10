# Print the elements of the list in a single line.

# Method 1
# * is the unpacking operator. Unpacks the list so the element passed as a seperate arguments.
def lst_single_line(lst):
  print(*lst,sep=",")

lst_single_line([1,2,3,4,5])
  
# Method 2
def lst_single_line(lst):
  for i in lst:
    print(i,end=" ")

lst_single_line([1,2,3,4,5])
