fi=open("NGUYENTO.INP")
fo=open("NGUYENTO.OUT", "w")

def sang(n):
    c=[True]*n
    c[0]=False
    p=2
    while p*p<=n:
        if c[p-1]==True:
            for i in range(p*p, n+1, p):
                c[i-1]=False
        p+=1
    return c

data=fi.readline().split()
n=int(data[0])
k=int(data[1])
ngto=sang(n)
cnt=0

for i in range(2, n):
    if ngto[i] == True:
        for p in range(i, n):
            if ngto[p] == True:
                if abs(p-i)==k:
                    cnt+=1

fo.write(f"{cnt}")