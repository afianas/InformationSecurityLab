def encrypt(text,a,b):
    result=""
    for c in text.upper():
        if c.isalpha():
            x=ord(c)-65
            result+=chr(((a*x+b)%26)+65)
    return result

def mod_inverse(a):
    for i in range(26):
        if(((a*i)%26)==1):
            return i

def decrypt(text,a,b):
    result=""
    a_inv=mod_inverse(a)
    for c in text:
        if c.isalpha():
            y=ord(c)-65
            result+=chr(((a_inv*(y-b))%26)+65)
    return result

text=str(input("Enter string:"))
a=int(input("Enter a"))
b=int(input("Ennter b"))


cipher=encrypt(text,a,b)
print(cipher)
plain=decrypt(cipher,a,b)
print(plain)