# Logical Operator

######  NOT #####
# not operator works on single operand
print(not True)   # Print False
print(not False)  # Print True

a = 10
b = 5
print(not (a > b)) # O/P False
print(not (a < b)) # O/P True

#### AND ####
# and operator works on two operand
and1 = True
and2 = False
and3 = True

print("AND Operator : ", and1 and and2) # O/P False
print("AND Operator : ", and1 and and3) # O/P True
print("AND Operator with expression : ", (a == b) and (a > b)) # O/P False
print("AND Operator with expression : ", (a == a) and (a > b)) # O/P True

#### OR ####
# or Operator works on two operand

or1 = True
or2 = False
or3 = True
or4 = False

print("OR Operator: ", or1 and or2) # O/P True
print("OR Operator: ", or1 and or3) # O/P True
print("OR Operator: ", or2 and or4) # O/P False
print("OR Operator with expression : ", (a == b) or (a > b)) # O/P True
print("OR Operator with expression : ", (a == b) or (a < b)) # O/P False
