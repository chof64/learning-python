shift = 3

message = "Hello World"

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
eUppercase = uppercase[shift:] + uppercase[:shift]

lowercase = "abcdefghijklmnopqrstuvwxyz"
eLowercase = lowercase[shift:] + lowercase[:shift]


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
