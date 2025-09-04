# Concatenate strings. Combining two or more strings are called concatenation.

name = "Arhan"
firstName = "Muhammad"
lastName = "Manzoor"
fullName = firstName+" "+name+" "+lastName
print(fullName) # O/P Muhammad Arhan

#====================
# Lenght of string
print(len(firstName)) # Print the count of total characters in the string

len1 = len(name)
print(len1)

len2 = len(fullName)
print(len2)           # Print the count of total characters in the string including spaces, special character etc..
#====================

# String Indexing
myCollege = "Bharathiar_University"
print(myCollege[0])  # Prints B
print(myCollege[2])  # prints a 

ch = myCollege[3]
print(ch)       # Prints r

#=======================

# String Slicing. Accessing the part of the string. Left to Right

myCollege = "Bharathiar_University"

print(myCollege[0:5])  # Prints Bhara
print(myCollege[1:5])  # Prints hara
print(myCollege[1:len(myCollege)])  # Prints harathiar_University
print(myCollege[1:])  # Prints harathiar_University. Translates into myCollege[1:len(myCollege)]
print(myCollege[:5]) # Prints Bhara. Translates into myCollege[0:5]

# Negative Index. From right to left of the string characters  -5 -4 -3 -2 -1
fruit = "Apple"

print(fruit[-3:-1])  # Print pl
print(fruit[-3:len(fruit)]) # Print ple
print(fruit[-len(fruit):])  # print the entire string

#===========================

str1 = "I am Manzoor"
str2 = "i am Male"

print(str1.endswith("or"))  # Prints True
print(str2.capitalize())    # print I am male Capitalize the firat letter of the string.









