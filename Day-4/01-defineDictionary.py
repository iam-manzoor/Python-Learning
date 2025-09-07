# Dict examples

info = {"name" : "Arhan", "age" : 9, "height" : 3.9, 12:"Intiger", 9.0 : "FLOAT"}

# Print Dictionary
print(info)

# Print particular value using "Key"
print(info["name"])    # Prints Arhan
print(info[12])        # Prints Intiger

# Assign new Value to the existing Key
info["name"] = "Muhammad Arhan"
print(info)

# Adding new key value pair
info["Country"] = "INDIA"
print(info)

# Create an empty Dictionary
details= {}
print(details)

# Adding values to the empty dict
details["name"] = "Arjun"
details["Age"]  = 12
