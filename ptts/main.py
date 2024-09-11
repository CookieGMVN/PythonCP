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

n=int(input())
ngto=sangngto(n)
ans=[]
for i in range(2, n+1):
    if ngto[i-1] == True:
        for i1 in range(2, int(n**.5)+2):
            if ngto[i1-1] == True and i1*i <= n and ans.count((i1*i)) == 0:
                ans.append(i1*i)

ans.sort()
print(ans)