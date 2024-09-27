import bisect
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

nha.sort()
dch.sort()

fi.close()
for i in nha:
    vt=bisect.bisect_left(dch, i)
    if vt==0:
        gn=dch[0]
    elif vt==len(dch):
        gn=dch[-1]
    else:
        gn=dch[vt-1] if dch[vt]-i > i-dch[vt-1] else dch[vt]
    kc=abs(gn-i)
    if kc > max_length:
        max_length=kc
        

fo.write(f"{max_length}")
fo.close()