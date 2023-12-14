# Author: Chad Fernandez
# License: MIT License

with open("grades.txt", "r") as f:
  contents = f.readlines()

print(contents)

print(type(contents))

for i in range(len(contents)):
  contents[i] = contents[i].strip()

print(contents)

counter = 0

students = []
grades = []

for i in contents:
  if i == "":
    continue

  if counter == 0:
    print("Name: " + i)
    students.append(i)
    counter += 1
  else:
    print("Grade: " + i)
    grades.append(i)
    counter = 0


print(students)
print(grades)

# get the index of the highest grade
print(grades.index(min(grades)))

highest_index = grades.index(min(grades))

highest_student = students[highest_index]
highest_grade = grades[highest_index]

print(highest_student, highest_grade)
