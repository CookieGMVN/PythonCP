fi=open("ENERGY.INP")
fo=open("ENERGY.OUT", "w")

n=int(fi.readline())
hgd=list(map(int, fi.readline().split()))

fi.close()
a=[]
b=[]
for i in range(0, len(hgd)):
    if hgd[i]%2==0:
        a.append(hgd[i])
    else:
        b.append(hgd[i])

a.sort()
b.sort()
fo.write(f"{max([a[int(len(a)/2)], b[int(len(b)/2)]])}")
fo.close()