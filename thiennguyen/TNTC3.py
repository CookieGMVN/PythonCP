fi=open("TNTC3.INP")
fo=open("TNTC3.OUT", "w")
x,y,m,n=list(map(int, fi.readline().split()))
fi.close()
d=0
for i in range(x, y+1):
    if i%m!=0 and i%n!=0:
        d+=1
fo.write(f"{d}")
fo.close()