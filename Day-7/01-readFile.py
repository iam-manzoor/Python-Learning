# Example to open a file and print the data.

# Simple open file and close it

file = open("demo.txt", "r")

file.close()

# file.read() print the whole file data

file = open("demo.txt", "r")

data = file.read()
print(data)
print(type(data))

file.close()

# file.read() speciifc character

file = open("demo.txt", "r")

data = file.read(5)   # Reads only the first 5 character of the file.
print(data)

data2 = file.read()   # Reads the remaining characters from the file.
print(data2)

file.close()

#file.readlines() Reads the data line by line.

file = open("demo.txt", "r")

line1 = file.readline()
print(line1)

line2 = file.readline()
print(line2)

file.close()

# Once the data read can not be read again unless we open the file again.

file = open("demo.txt", "r")

data = file.read()            # Reads the whole content of the file
print(data)                   # Prints the whole content

line1 = file.readline() 
print(line1)                  # Prints the empty space, because the content is already read

line2 = file.readline()
print(line2)                  # Prints the empty space, because the content is already read

file.close()

