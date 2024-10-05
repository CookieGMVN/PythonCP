fi=open("SOTHOC.INP")
fo=open("SOTHOC.OUT", "w")
c=2023
n,q=list(map(int, fi.readline().strip().split()))
fi.close()
mod=q%c
u=1
s=1
for k in range (1,n):
    u=((u%c)*mod)%c
    s=(s%c+u)%c
fo.write(str(s))
fo.close()