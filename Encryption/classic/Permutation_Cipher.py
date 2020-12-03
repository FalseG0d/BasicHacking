def decrypt(cipher, ciphertext):
    return encrypt(inverse_key(cipher), ciphertext)

def encrypt(cipher, plaintext):
    plaintext = "".join(plaintext.split(" ")).upper()
    ciphertext = ""
    for pad in range(0, len(plaintext)%len(cipher)*-1%len(cipher)):
        plaintext += "X"
    for offset in range(0, len(plaintext), len(cipher)):
        for element in [a-1 for a in cipher]:
            ciphertext += plaintext[offset+element]
        ciphertext += " "
    return ciphertext[:-1]

def inverse_key(cipher):
    inverse = []
    for position in range(min(cipher),max(cipher)+1,1):
        inverse.append(cipher.index(position)+1)
    return inverse

#To encrypt, run:

cipher = [2,4,1,5,3]
plaintext = "LOREM IPSUM DOLOR SITAM ETCON SECTE TUERA DIPIS CINGE LITXX"
ciphertext = encrypt(cipher, plaintext)

print("[*] Cipher Text: \t"+ciphertext)

plaintext = decrypt(cipher, ciphertext)

print("[*] Plain Text: \t"+plaintext)