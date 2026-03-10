def generate_key(text,key):
    key=list(key)
    for i in range(len(text)-len(key)):
        key.append(key[i%len(key)])
    return "".join(key)

def encrypt(text,key):
    result=""
    for i in range(len(text)):
        result+=chr(((ord(text[i])-65+ord(key[i])-65)%26)+65)
    return result

def decrypt(text,key):
    result=""
    for i in range(len(text)):
        result+=chr((((ord(text[i])-65)-(ord(key[i])-65)+26)%26)+65)
    return result

text=str(input("Enter string:"))
text=text.upper()

k=str(input("Enter key"))
key=generate_key(text,k)
key=key.upper()
cipher=encrypt(text,key)
print(cipher)
plain=decrypt(cipher,key)
print(plain)