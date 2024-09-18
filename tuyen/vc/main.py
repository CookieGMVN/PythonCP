fi=open("vc.inp")
fo=open("vc.out", "w")

data=fi.readlines()
n=int(data[0].split()[0])
k=int(data[0].split()[1])
toa=list(map(int, data[1].split()))
sothung=0
ngay=0
while sothung<sum(toa):
    sothung+=n*k
    ngay+=1
fo.write(f"{ngay}")
fo.close()
fi.close()