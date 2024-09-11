n=int(input())
index=1
s1=0
s2=1
ns=s2

while index<n:
    index+=1
    s1,s2=s2,ns
    ns=s1+s2
print(ns)