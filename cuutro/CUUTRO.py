def modify(remaining, l, r, k):
    i=l-1
    while i<r:
        remaining[i]+=k
        i+=1
    return remaining

fi=open("CUUTRO.INP")
fo=open("CUUTRO.OUT", "w")
n,q=list(map(int, fi.readline().strip().split()))
remaining=list(map(int, fi.readline().strip().split()))
final=""
data=fi.readlines()
fi.close()
for i in data:
    l,r,k=list(map(int, i.strip().split()))
    remaining = modify(remaining, l, r, k)
fo.write(" ".join(map(str, remaining)))
fo.close()