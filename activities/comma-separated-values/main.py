# Author: Chad Fernandez
# License: MIT License


# OPEN INPUT FILE
# We use the with statement to open the file. This is the preferred way as it
# will automatically close the file for us when we are done with it.
with open("data.txt", "r") as f:
  contents = f.readlines()


items = []

# STRIP NEWLINE CHARACTERS
# Each element in the list has a newline character at the end. We can use the
# strip() method to remove the newline character.
for i in range(len(contents)):
  for thing in contents[i].strip().split(", "):
    items.append(thing)


# SORT LIST
# Sort the list alphabetically.
items.sort()


# OPEN/CREATE OUTPUT FILE
# We use the with statement to open the file. This is the preferred way as it
#
# This line will create a new file called "output.txt" if it does not exist.
#
# We use the join() method to join the elements in the list into a string. The
# delimiter is ", " (comma and a space). This converts the list into a string.
with open("output.txt", "w") as f:
  f.write(", ".join(items))
