# Author: Chad Fernandez
# License: MIT License
# Description: This is a brute force attack. It will try every possible key to
# decrypt the message. It will print the decrypted message for each key. You
# will have to look through the results to find the correct message.


# USER INPUT
# Get input from the user for the message to brute force decrypt.
message = input("Enter a message to brute force decrypt: ")
print("\n")

# OUR ALPHABET
# This is the base alphabet that we will shift to encrypt the mssage.
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

# DECRYPT FUNCTION
# This function takes a message as an argument and returns the decrypted
# message.
#
# It loops through each letter in the message and checks if it is in the
# encrypted uppercase or lowercase alphabet. If it is, it gets the index of
# that letter in the encrypted alphabet and uses that index to get the
# decrypted letter from the alphabet. If the letter is not in the encrypted
# alphabet, it just adds the letter to the result.
#
# This is the exact opposite of the encrypt function.
def decrypt(message):
    result = ""
    for letter in message:
        if letter in eUppercase:
            result += uppercase[eUppercase.index(letter)]
        elif letter in eLowercase:
            result += lowercase[eLowercase.index(letter)]
        else:
            result += letter
    return result

# BRUTE FORCE
# Loop through every possible key.
for key in range(26):
  # This is the new encrypted alphabet. We use slicing to shift the alphabet
  # by the key.
  eUppercase = uppercase[key:] + uppercase[:key]
  eLowercase = lowercase[key:] + lowercase[:key]

  # Call the decrypt function and put the result in variable.
  decrypted = decrypt(message)

  # Print the results.
  print("KEY: ", key)
  print("DECRYPTED: ", decrypted,"\n")
