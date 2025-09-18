# Methods Example

collection = set()

# .add Method
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("Arhan")
collection.add((1,2,3))

print(collection)                 # Prints {1,2,"Arhan",(1,2,3)}

# Accessing the set() value
set1 = {1,2,"Arhan",(1,2,3)}
my_list = list(set1)
print(my_list[0])
print(my_list[-1])

# .remove Method
collection.remove(2)

print(collection)                 # prints {2}

# Try to remove the values which doesnt exist in set

collection.remove(7)             # prints KeyError (value doesnt exist)

# Adding List in set

collection.add([1,2,3])          # unhashable type - Error. The hash of the var doesnt change. List is muttable its tend to change the hash value

# .pop Method

print(collection.pop())           # Removes the random value.
print(collection.pop())

# .union Method

print(collection.union(collection2))    # Combines both set values & return new. Contains values from bith set not duplicates.

# .intersection Method

print(collection.intersection(collection2))  # Comman values in the form of new set.

# .clear Method

collection.clear()        # Empty the set.
