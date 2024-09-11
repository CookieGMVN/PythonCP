fi=open("data.inp")
fo=open("data.out", "w")

data=fi.readlines()
n=int(data[0].split()[0])
k=int(data[0].split()[1])
xe=list(map(int, data[1].split()))
kq=[]

for i in range(0, len(xe)):
    if xe[i] > k:
        kq.append(f"{i+1} {xe[i]-k}")

if len(kq)==0:
    fo.write("0")
else:
    fo.write("\n".join(kq))
fo.close()
fi.close()