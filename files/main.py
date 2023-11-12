# with open("./samefolder.txt", "r") as f:
#     print(f.read())

contents = """
LIBRARY

Name: Chad Fernandez
Title: Just a Cool Title
"""

with open("./library.txt","w") as f:
  f.write(contents)
