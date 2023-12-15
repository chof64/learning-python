# Author: Chad Fernandez
# License: MIT License


# OPEN FILE
# We use the with statement to open the file. This is the preferred way as it
# will automatically close the file for us when we are done with it.
#
# Read more: https://www.geeksforgeeks.org/with-statement-in-python
#
# The "r" (second argument) means we are opening the file for reading
# (read mode). Then we assign the file object to the variable f.
with open("grades.txt", "r") as f:

  # READLINES
  # This will read the entire file line by line and return a list of strings.
  # Each element in the list is a line from the file.
  contents = f.readlines()


# (Optional): Uncomment the lines below.
# print(contents)
# print(type(contents))


# STRIP NEWLINE CHARACTERS
# Each element in the list has a newline character at the end. We can use the
# strip() method to remove the newline character.
#
# Newline characters are represented by "\n" and it is a special character that
# tells the computer to move to the next line.
#
# We strip the newline character because it is causing problems when we try to
# loop through the list. And will cause problems when we try to convert the
# strings to integers.
for i in range(len(contents)):
  contents[i] = contents[i].strip()


# (Optional): Uncomment the lines below.
# print(contents)


# DECLARE VARIABLES
# These variables will be used to keep track of the student name and grade, and
# will be updated as we loop through the list.
#
# We start the counter at 0 because we know the first element in the list is a
# student name. Our code will check if the counter is 0 or 1 to determine if it
# is a student name or grade.
counter = 0
students = []
grades = []

for i in contents:

  # SKIP EMPTY STRINGS
  # This will skip any empty strings. We know there are empty strings in the
  # list because we removed the newline characters. So if there are two
  # consecutive newline characters, it will result in an empty string.
  if i == "":
    continue

  # CHECK COUNTER
  # By default, the counter is 0. A 0 counter means it is a student name. A 1
  # counter means it is a grade.
  if counter == 0:
    # (Optional): Uncomment the lines below.
    # print("Name: " + i)

    # APPEND
    # We append the student name to the list of students.
    students.append(i)

    # UPDATE COUNTER
    # We update the counter to 1 because we know the next element in the list
    # will be a grade. Specifically, the grade for the student we just added to
    counter += 1
  else:
    # (Optional): Uncomment the lines below.
    # print("Grade: " + i)

    # APPEND
    # We append the grade to the list of grades.
    grades.append(i)

    # UPDATE COUNTER
    # We update the counter to 0 because we know the next element in the list
    # will be a student name.
    counter = 0


# (Optional): Uncomment the lines below.
# print(students)
# print(grades)


# GET THE HIGHEST GRADE
# We use the min() function to get the highest grade. The min() function will
# compare all the grades and return the lowest value.
#
# Note: Don't forget that in our grading system, 1 is the highest grade. Don't
# get confused with the min() function.
#
# We then use the index() method to get the index of the highest grade. Which
# we will use to get the student name.
highest_index = grades.index(min(grades))


# GET THE STUDENT NAME
# We use the index, the one that we got from the previous step, to get the
# student name and grade from their respective lists.
highest_student = students[highest_index]
highest_grade = grades[highest_index]


# PRINT THE HIGHEST GRADE
print(highest_student, highest_grade)
