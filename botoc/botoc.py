fi=open("DATA.INP")
fo=open("DATA.OUT", "w")

inp=list(map(int, fi.readline().split()))
ans=list(set(inp))

botoc=0

for i in ans:
    if inp.count(i)%i==0:
        botoc+=inp.count(i)/i
    
fo.write(str(int(botoc)))
fo.close()
fi.close()