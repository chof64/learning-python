# Author: Chad Fernandez
# License: MIT License
# Description: This focuses on decryption. Decrypts a message using the Ceasar
# Cipher.


# USER INPUT
# Get input from the user for the key and message to decrypt.
key = int(input("Enter a number to shift by (the key): "))
message = input("Enter a message to decrypt: ")
print("\n")

# OUR ALPHABET
# This is the base alphabet that we will shift to encrypt the mssage.
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

# This is the new encrypted alphabet. We use slicing to shift the alphabet by
# the key.
eUppercase = uppercase[key:] + uppercase[:key]
eLowercase = lowercase[key:] + lowercase[:key]

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

# DECRYPT
# Call the decrypt function and put the result in variable.
decrypted = decrypt(message)

# PRINT RESULTS
print("\nPLAIN TEXT: ", message)
print("KEY: ", key,"\n")

print("DECRYPTED: ", decrypted)
