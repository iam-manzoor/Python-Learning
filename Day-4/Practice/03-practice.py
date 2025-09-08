# WAP to enter marks of 3 subject from the user and store them in a dictionary. STart with an empty dictionary and add one by one. Use subject name as key and marks as value.

marks = {}


x = int(input("Enter Phy : "))
marks.update({"phy" : x})

x = int(input("Enter Math : "))
marks.update({"Math" : x})

x = int(input("Enter Che : "))
marks.update({"Che" : x})

print(marks)
