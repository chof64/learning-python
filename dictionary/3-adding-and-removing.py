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

print("\n", myinformation)

# myinformation.update({"Name": "Chad F."})

myinformation["Name"] = "Chad F."

print("\n", myinformation)


with open("./contents.txt","w") as f:
  f.write(str(myinformation))
