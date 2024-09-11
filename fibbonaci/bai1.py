n=int(input())
s1=0
s2=1
ns=s2  
lm=1

while ns <= n:
    print(ns, end=" ")
    lm += 1
    s1,s2 = s2, ns
    ns = s1 + s2
print()