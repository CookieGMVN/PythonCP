fi=open("CHIAMANG.INP")
fo=open("CHIAMANG.OUT", "w")
n=int(fi.readline())
mang=list(map(int, fi.readline().strip().split()))
fi.close()
i=0
tong=0
nuamang=sum(mang)/2
while tong<nuamang:
    tong+=mang[i]
    i+=1
if tong!=nuamang:
    fo.write(f"0")
else:
    fo.write(f"{i}")
fo.close()