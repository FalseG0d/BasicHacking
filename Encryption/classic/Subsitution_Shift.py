import random

# Subsitution Cipher

alphabet="'abcdefghijklmnopqrstuvwxyz.,!'" 

def listToString(s):
    str1 = ""  
    for ele in s:  
        str1 += ele      
    return str1 

def makeKey(alphabet):
	alphabet=list(alphabet)
	random.shuffle(alphabet)
	alphabet=str(alphabet)
	return alphabet

print("\nOriginal Text:\t"+alphabet)

s=makeKey(alphabet)
sub_alpha=listToString(s)

print("\n\nEncrypted Text:\t"+sub_alpha)

print(type(s))

print("\n\nKeys:\n")
for i in range(len(alphabet)):
    print(alphabet[i]+":"+sub_alpha[i],end='\t')
