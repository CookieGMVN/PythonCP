fi=open("DATA.INP")
fo=open("DATA.OUT", "w")

inp=fi.readlines()
arr=list(map(int, inp[1].split()))

ck=arr[0]
mx=arr.count(ck)
for i in arr:
    if i!=ck:
        ck=i
        if arr.count(ck) > mx:
            mx=arr.count(ck)

fo.write(str(mx))
fi.close()
fo.close()