fi=open("SHIPPING.INP")
fo=open("SHIPPING.OUT", "w")

data=list(map(int, fi.readline().split()))
n=data[0]
m=data[1]
nha=[]
dch=[]
max_length=0

data=list(map(int, fi.readline().split()))
for i in data:
    nha.append(i)

data=list(map(int, fi.readline().split()))
for i in data:
    dch.append(i)

fi.close()
for i in nha:
    kc=10e6
    for j in dch:
        if kc > abs(i-j):
            kc=abs(i-j)
    if max_length < kc:
        max_length=kc

fo.write(f"{max_length}")
fo.close()