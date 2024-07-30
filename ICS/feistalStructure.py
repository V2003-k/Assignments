import binascii

def rand_key(p):
    import random
    key1 = ""
    p = int(p)
    for i in range(p):
        temp = random.randint(0, 1)
        temp = str(temp)
        key1 = key1 + temp
    return key1

def exor(a, b):
    temp = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            temp += "0"
        else:
            temp += "1"
    return temp

def BinaryToDecimal(binary):
    string = int(binary, 2)
    return string

PT = input("Enter Plain Text: ")
print("Plain Text is:", PT)

PT_Ascii = [ord(x) for x in PT]
PT_Bin = [format(y, '08b') for y in PT_Ascii]
PT_Bin = "".join(PT_Bin)

n = len(PT_Bin) // 2
L1 = PT_Bin[:n]
R1 = PT_Bin[n:]
m = len(R1)

K1 = rand_key(m)

f1 = exor(R1, K1)
R2 = exor(f1, L1)
L2 = R1

bin_data = L2 + R2
str_data = ''

for i in range(0, len(bin_data), 7):
    temp_data = bin_data[i:i + 7]
    decimal_data = BinaryToDecimal(temp_data)
    str_data += chr(decimal_data)

print("Cipher Text:", str_data)

L3 = L2
R3 = R2

f2 = exor(L3, K1)
L4 = exor(R3, f2)
R4 = L3
PT1 = L4 + R4

PT1 = int(PT1, 2)
RPT = binascii.unhexlify('%x' % PT1)
print("Retrieved Plain Text is:", RPT.decode())
