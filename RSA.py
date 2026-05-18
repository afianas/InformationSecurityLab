def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def mod_inverse(e,phi):
    for d in range(1,phi):
        if((e*d)%phi==1):
            return d


def generate_keys():
    p=int(input("P:"))
    q=int(input("Q"))
    n=p*q
    phi=(p-1)*(q-1)
    posse=[]
    for e in range(2,phi):
        if (gcd(e,phi)==1):
            posse.append(e)
    print(posse)
    e=int(input("Select a value of e"))
    d=mod_inverse(e,phi)  
    print(f"{d,n}")
    print(f"{e,n}")
    return (d,n),(e,n)

def encrypt(text,publ):
    e,n=publ
    cip=pow(text,e,n)
    return cip

def decrypt(text,priv):
    d,n=priv
    dec=pow(text,d,n)
    print(dec)


priv,publ=generate_keys()
text=int(input("enter to be deciphered"))
cip=encrypt(text,publ)
print(cip)
decrypt(cip,priv)
