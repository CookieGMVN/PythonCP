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

fi=open("fibonacci.inp")
fo=open("fibonacci.out", "w")

m=int(fi.readline())

ngto=sangngto(m+1)
s1=0
s2=1
ns=0
fibonacci=[]

while ns <= m:
    fibonacci.append(ns)
    s1,s2 = s2, ns
    ns = s1 + s2

c=0
for i in fibonacci:
    if ngto[i-1] == True and c<i:
        c=i

fo.write(" ".join(map(str, fibonacci)))
fo.write(f"\n{c}")