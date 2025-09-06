# Examples of few methods supported by List.

marks = [89,53,98,42,67]

marks.append(71)             # Adds the element at the end of the list. [89,53,98,42,67,71]
marks.sort()                 # Sort the list in ascending order 
marks.sort(reverse=True)     # Same as above sort
marks.reverse()              # Prints the list in the reverse order
marks.insert(3,75)           # Insert the element 75 in the third index of the list. [89,53,98,75,42,67,71]
marks.pop()                  # Removes the last element from the list.
marks.pop(2)                 # Removes the element which is in index 2
marks.count(42)              # Prints the count of the given element in the list.

# Methods supported by Python list
print(dir(list))
