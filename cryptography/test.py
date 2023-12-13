shift = 5

message = "Hello World"

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
eUppercase = uppercase[shift:] + uppercase[:shift]

lowercase = "abcdefghijklmnopqrstuvwxyz"
eLowercase = lowercase[shift:] + lowercase[:shift]

print(uppercase)
print(eUppercase)
print(lowercase)
print(eLowercase)

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

print(encrypt(message))
