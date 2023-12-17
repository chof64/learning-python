# Author: Chad Fernandez
# License: MIT License


with open("input.txt", "r") as f:
  contents = f.readlines()

for i in range(len(contents)):
  contents[i] = contents[i].strip()


# Use the reverse() method to reverse the list.
contents.reverse()


with open("output.txt", "w") as f:
  # Use the join() method to join the elements in the list into a string. The
  # delimiter is "\n" (newline character). This converts the list into a string.
  f.write("\n".join(contents))
