# Palindrome Script

# Method-1
lst = [1,2,3,2,1]
lst_reverse = lst.copy()
lst_reverse.reverse()

if lst == lst_reverse:
  print("List is a Palindrome")

# Method-2
lst = [1,2,3,2,1]

if lst == lst[::-1]:
  print("List is palindrome")
else:
  print("List is not palindrome")

# String Palindrome

str = "madam"
if str == str[::-1]:
  print(f'string "{str}" is palindrome')
else:
  print('string "{}" is not palindrome'.format(str))

