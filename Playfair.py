def create_matrix(key):
    key=key.upper().replace("I","J")
    matrix=[]
    used=set()
    for c in key:
        if c not in used:
            used.add(c)
            matrix.append(c)
    for c in "ABCDEFGHJKLMNOPQRSTUVWXYZ":
        if c not in used:
            used.add(c)
            matrix.append(c)
    return [matrix[i:i+5] for i in range(0,25,5)]


def find(matrix,c):
    for i in range(5):
        for j in range(5):
            if (matrix[i][j]==c):
                return i,j
def encrypt(text,matrix):
    result=""
    text = text.replace("I","J")
    if len(text)%2!=0:
        text+= "X"
    for i in range(0,len(text),2):
        a,b=text[i],text[i+1]
        r1,c1=find(matrix,a)
        r2,c2=find(matrix,b)

        if r1==r2:
            result+=matrix[r1][(c1+1)%5]
            result+=matrix[r2][(c2+1)%5]
        elif c1==c2:
            result+=matrix[(r1+1)%5][(c1)]
            result+=matrix[(r2+1)%5][(c2)]
        else:
            result+=matrix[r1][c2]
            result+=matrix[r2][c1]
    return result

def decrypt(text,matrix):
    result=""
    for i in range(0,len(text),2):
        a,b=text[i],text[i+1]
        r1,c1=find(matrix,a)
        r2,c2=find(matrix,b)

        if r1==r2:
            result+=matrix[r1][(c1-1)%5]
            result+=matrix[r2][(c2-1)%5]
        elif c1==c2:
            result+=matrix[(r1-1)%5][(c1)]
            result+=matrix[(r2-1)%5][(c2)]
        else:
            result+=matrix[r1][c2]
            result+=matrix[r2][c1]
    return result

text=str(input("Enter string:")).upper()
key=str(input("Enter key"))
matrix=create_matrix(key)

cipher=encrypt(text,matrix)
print(cipher)
plain=decrypt(cipher,matrix)
print(plain)