"""
# Accessing a dictionary

# You can access the items of a dictionary by referring to its key name, inside
# the square brackets.
"""


# Creating a dictionary with values to use in the examples.
myinformation = {
  "Name": "Chad",
  "Age": 20,
  "Male": True,
  "Hobbies": ["Coding", "Gaming", "Reading"],
  "Pets": {
    "Dog": "Buddy",
    "Cat": "Misty",
    "Bird": {
      "Name": "Tweety",
      "Age": 1
    }
  }
}

print("\n",myinformation)

# Accessing the Pets key.
print("\n",myinformation["Pets"])

print("\n",myinformation["Pets"]["Bird"])

print("\n",myinformation["Pets"]["Bird"]["Age"])

# Accessing the Hobbies key.
print("\n",myinformation["Hobbies"])

print("\n",myinformation["Hobbies"][0])

# print(myinformation.keys())
