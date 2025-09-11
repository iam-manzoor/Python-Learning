# Examples of write and appen mode 

# write operation

f = open("demo.txt", "w")

f.write("I am a write operation")

f.close()

# Append operation

f.open("demo.txt", "a")

f.write("\nI am the append operation")

f.close()
