fi=open("DATA.INP")
fo=open("DATA.OUT", "w")

inp=fi.readlines()
arr=inp[1].split()

t=0
for i in arr:
    if int(i)%2==1:
        t+=int(i)
fo.write(str(t))
fi.close()
fo.close()