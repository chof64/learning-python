# Author: Chad Fernandez
# License: MIT License
# Description: This focuses on encryption. Encrypts a message using the Ceasar
# Cipher.


# USER INPUT
# Get input from the user for the key and message to encrypt.
key = int(input("Enter a number to shift by (the key): "))
message = input("Enter a message to encrypt: ")

# OUR ALPHABET
# This is the base alphabet that we will shift to encrypt the mssage.
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

# This is the new encrypted alphabet. We use slicing to shift the alphabet by
# the key.
eUppercase = uppercase[key:] + uppercase[:key]
eLowercase = lowercase[key:] + lowercase[:key]

# ENCRYPT FUNCTION
# This function takes a message as an argument and returns the encrypted
# message.
#
# It loops through each letter in the message and checks if it is in the
# uppercase or lowercase alphabet. If it is, it gets the index of that letter
# in the alphabet and uses that index to get the encrypted letter from the
# encrypted alphabet. If the letter is not in the alphabet, it just adds the
# letter to the result.
def encrypt(message):
    result = ""
    for letter in message:
        if letter in uppercase:
            result += eUppercase[uppercase.index(letter)]
        elif letter in lowercase:
            result += eLowercase[lowercase.index(letter)]
        else:
            result += letter
    return result

# ENCRYPT
# Call the encrypt function and put the result in variables.
encrypted = encrypt(message)

# PRINT RESULTS
print("\nPLAIN TEXT: ", message)
print("KEY: ", key,"\n")

print("ENCRYPTED: ", encrypted,"\n")