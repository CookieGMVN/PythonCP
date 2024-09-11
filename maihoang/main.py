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
            

fi=open("DATA.INP")
fo=open("DATA.OUT", "w")

inp=list(map(int, fi.readline().split()))
ngto=sangngto(max(inp))

mai=0
hoang=0
for i in range(inp[0], inp[1] + 1):
    if ngto[i-1] == True:
        mai+=1
for i in range(inp[2], inp[3] + 1):
    if ngto[i-1] == True:
        hoang+=1

if mai > hoang:
    fo.write(f"Mai thắng, số lượng: {mai}")
elif hoang > mai:
    fo.write(f"Hoàng thắng, số lượng: {hoang}")
else:
    fo.write(f"Hòa, số lượng: {mai}")
fo.close()
fi.close()