fi=open("LAISUAT.INP")
fo=open("LAISUAT.OUT", "w")
n,s=list(map(int, fi.readline().strip().split()))
dsls=list(map(int, fi.readline().strip().split()))
dsls.append(0)
tongls=0
songay=[]
ngayht=0
for ls in dsls:
    if ls==s:
      songay.append(1)
      ngayht=0
      tongls=0
    if tongls>=s:
        songay.append(ngayht)
        ngayht=0
        tongls=0
    else:
        tongls+=ls
        ngayht+=1
if len(songay)<=0:
    fo.write("-1")
else:
    fo.write(str(min(songay)))