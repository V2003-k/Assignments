 
def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif(char.islower()):
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - key - 65) % 26 + 65)
        elif(char.islower()):
            result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char
    return result

text = input("Enter your text: ")
print(text)
key = int(input("Enter your key value: "))
print(key)

print ("Text  : " + text)
print ("Shift : " + str(key))
print ("Cipher: " + encrypt(text, key))
text1 = encrypt(text, key)
print ("Decrypt: " + decrypt(text1, key))