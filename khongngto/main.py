def sangngto(n):
    ngto=[True]*n
    ngto[0]=False
    p=2
    while p*p<=n:
        if ngto[p-1]==True:
            for i in range(p*p, n+1, p):
                ngto[i-1]=False
        p+=1
    return ngto

fi=open("knt.inp")
fo=open("knt.out", "w")

n=int(fi.readline())
ngto=sangngto(n+1)
uoc=[1]

for i in range(2, int(n/2)+1):
    if n%i==0 and ngto[(i-1)]==False:
        uoc.append(i)

if ngto[n-1] == False:
    uoc.append(n)

fo.write(f"{len(uoc)}")
fo.close()
fi.close()