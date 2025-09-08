# Dicit Methods

info = {"name" : "Arhan", "age" : 9, "height" : 3.9, 12:"Intiger", 9.0 : "FLOAT"}

# .keys Method
print(info.keys())                  # Prints All the keys from the dict
print(list(info.keys()))            # Prints the keys in the List format

# Print the length of the dict
print(len(info))
print(len(list(info.keys())))       # Nested functions in Python.

# .values Method
print(info.values())                # Prints All the values from the dict.
print(list(info.values()))          # Prints the values in the List format.

# .items Method.
pairs = info.items()                # Assign the items (key & value) to pairs var in the tuple format.
print(pairs[0])                     # Access the tuple values using index.

# .get Method
print(info.get("name"))             # Prints the value of the key name. Returns None in case the key is not present
                                    # Exection will continue.
print(info["name"])                 # Also prints the value of the key. Returns error in case the key is not present
                                    # Once its error out the execution will fail.

# .update Method.
info.update({"city":"Chennai"})
print(info)

# List the Dict methods
print
