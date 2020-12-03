# AShift Cipher

def AShiftEncrypt(text,s):
    print("[*] Original Message: "+text)
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


print("[*] Encrypted Text: "+AShiftEncrypt('abcdefghijklmnopqrstuvwxyz.,!',4))