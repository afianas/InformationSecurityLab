import numpy as np
def encrypt(text,key):
    text=text.upper().replace(" ","")
    if len(text)%2!=0:
        text+="X"
    result=""
    for i in range(0,len(text),2):
        pair=[ord(text[i])-65,ord(text[i+1])-65]
        res=np.dot(key,pair)%26

        result+=chr(res[0]+65)
        result+=chr(res[1]+65)
    return result

def decrypt(text,key):
    result=""
    det=int(round(np.linalg.det(key)))
    det_inv=pow(det, -1, 26)

    key_inv=det_inv*(np.round(det * np.linalg.inv(key)).astype(int)) % 26

    for i in range(0,len(text),2):
        pair=[ord(text[i])-65,ord(text[i+1])-65]
        res=np.dot(key_inv,pair)%26
        result+=chr(res[0]+65)
        result+=chr(res[1]+65)        
    return result
text = input("Enter plaintext: ")

print("Enter key matrix (2x2):")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

key = [[a, b],
       [c, d]]

cipher = encrypt(text, key)
print("Encrypted:", cipher)

plain = decrypt(cipher, key)
print("Decrypted:", plain)