def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def mod_inverse(e,phi):
    for i in range(1,phi):
        if((e*i)%phi)==1:
            return i
def generate_keys():
    p=int(input("P:"))
    q=int(input("Q:"))
    n=p*q
    phi=(p-1)*(q-1)
    posse=[]

    for e in range(2,phi):
        if gcd(e,phi)==1:
            posse.append(e)
    print(posse)
    e=int(input("select e"))

    d=mod_inverse(e,phi)

    return (d,n),(e,n)

def encrypt(text,priv):
    d,n=priv
    return pow(text,d,n)
def decrypt(text,pub):
    e,n=pub
    return pow(text,e,n)


def simple_hash(message):
    hashval=0
    for c in message:
        hashval=hashval*31+ord(c)
    return hashval

priv,pub=generate_keys()
e,n=pub
message=str(input("Enter"))
hash_val=simple_hash(message)
print(hash_val)
signature=encrypt(hash_val,priv)
print(signature)
verif=decrypt(signature,pub)
print(verif)
new=simple_hash(message)

if verif==new%n:
    print("verified")
else:
    print("not")
