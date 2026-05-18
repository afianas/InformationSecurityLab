import hashlib
s1=str(input("Enter string"))
h1=hashlib.sha256(s1.encode()).hexdigest()
print(h1)
s2=str(input("Enter string"))
h2=hashlib.sha256(s2.encode()).hexdigest()
print(h2)
h1_bytes=bytes.fromhex(h1)
h2_bytes=bytes.fromhex(h2)
h1b=int.from_bytes(h1_bytes,byteorder="big")
h2b=int.from_bytes(h2_bytes,byteorder="big")
xored=h1b^h2b
rr=bin(xored).count('1')
print(rr)