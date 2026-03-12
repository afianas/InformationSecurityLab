def encrypt(text,key):
    result=""
    for c in text.upper():
        if c.isalpha():
            result+=chr(((ord(c)-65+key)%26)+65)
    return result

def decrypt(text,key):
    result=""
    for c in text.upper():
        if c.isalpha():
            result+=chr(((ord(c)-65-key)%26)+65)
    return result

text=str(input("Enter string:"))
key=int(input("Enter key"))

cipher=encrypt(text,key)
print(cipher)
plain=decrypt(cipher,key)
print(plain)
