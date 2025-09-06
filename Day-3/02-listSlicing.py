# Below are the example of list slicing.

marks = [89,64,78,99,97]
print(marks[1:4])         # Prints 64,78,99
print(marks[:4])          # Prints 89,64,78,99 Is as same as [0:4]
print(marks[:len(marks)]) # prints 89,64,78,99,97
print(marks[1:])          # Same as line number 6. prints 89,64,78,99,97
      
# Negative Indexing in List
print(marks[-3:-1])       # Prints 78,99
print(marks[-1:])         # Prints 97. The last element.
print(marks[-5:])         # print 89,64,78,99,97. The entire list
