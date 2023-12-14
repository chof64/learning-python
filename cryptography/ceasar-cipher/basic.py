# Author: Chad Fernandez
# License: MIT License
# Description: Encrypts a message using the Ceasar Cipher. This is a basic
# implementation of the Ceasar Cipher. Which uses slicing to shift the alphabet
# by a given number of letters.


# USER INPUT
# Get input from the user for the key and message to encrypt.
key = int(input("Enter a number to shift by (the key): "))
message = input("Enter a message to encrypt: ")
print("\n")

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

# ENCRYPT AND DECRYPT
# Call the encrypt and decrypt functions and put the results in variables.
encrypted = encrypt(message)
decrypted = decrypt(encrypted)

# PRINT ALPHABETS
# print("PLAIN UPPER: ", uppercase)
# print("ENCRYPTED UPPER: ", eUppercase, "\n")
#
# print("PLAIN LOWER: ", lowercase)
# print("ENCRYPTED LOWER: ", eLowercase,"\n")

# PRINT RESULTS
print("PLAIN TEXT: ", message)
print("KEY: ", key,"\n")

print("ENCRYPTED: ", encrypted,"\n")

print("DECRYPTED: ", decrypted)
