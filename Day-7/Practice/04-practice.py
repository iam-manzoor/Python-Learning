# Return the line number of the word first existance

def find_line_number():
  word = "learning"
  data = True
  line_no = 1
  with open("practice.txt", "r") as f:
    while data:
      data = f.readline()
      if word in data :
        print(line_no)
        return
      line_no += 1
  return -1

print(find_line_number())
