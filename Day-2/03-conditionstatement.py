# Executed block of code when the condition is True

# if condition
myAge = 21

if(myAge >= 18): # Executes when the condition is met.
  print("Can Vote")
  print("Can Drive")

if(True):       # Always Executes
  print("Can Vote")
  print("Can Drive")

#=============================

# if else 

if(myAge >= 18): # Executes when the condition is met.
  print("Can Vote")
  print("Can Drive")
else:
  print("you will be eligible in {} years".format(18 - myAge))

#==============================

# if - elif - else

trafficLight = "Red"

if(trafficLight == "Red"):
  print("Stop")
elif(trafficLight == "Green"):
  print("Go")
elif(trafficLight == "Yellow"):
  print("Watch Out")
else:
  print("Traffic Light malfunction")

#============================

# Nesting condition statement

age = 18
if age >= 18:
  if age >= 80:
    print("Cant Drive")
  else:
    print("Can drive")
else:
  print("Cant drive")

#============================

# Grade Student based on marks
mark = int(input("Enter the mark : "))

if mark >= 90:
  print("Grade A")
elif mark < 90 and mark >= 80:
  print("Grade B")
elif mark < 80 and mark >= 70:
  print("Grade C")
elif mark < 70 and mark >= 60:
  print("Grade D")
else:
  print("Grade F")
  
  
