# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all the students.

# Method 1
student_1 = {"python","java","C++","python","javascript"}
student_2 = {"java","python","java","C++","C"}

classrooms = len(student_1.union(student_2))

print(classrooms)

# Method 2

subjects = {
  "python","java","C++","python","javascript",
  "java","python","java","C++","C"
}

print(len(subjects))
