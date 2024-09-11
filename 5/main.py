fi=open("DATA.INP")
fo=open("DATA.OUT", "w")

inp=fi.readlines()
arr=list(set(map(int, inp[1].split())))
kq_chan=[]
kq_le=[]

for i in arr:
    if i%2==0:
        kq_chan.append(i)
    else:
        kq_le.append(i)

if len(kq_chan) == 1:
    fo.write(str(kq_chan[0]))
else:
    fo.write(str(kq_le[0]))

fi.close()
fo.close()