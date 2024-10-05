fi=open("CHIAKEO.INP")
fo=open("CHIAKEO.OUT", "w")
n,m=list(map(int, fi.readline().strip().split()))
dshs=list(map(int, fi.readline().strip().split()))
queue=[]
fi.close()
for hs in dshs:
    queue.append({ "want": hs, "current": hs })
while len(queue) > 1:
    if queue[0]["current"]<=m:
        queue.pop(0)
    else:
        remainingCandies={"want": queue[0]["want"], "current": queue[0]["current"]-m}
        queue.pop(0)
        queue.append(remainingCandies)
fo.write(str(dshs.index(queue[0]["want"])+1))
fo.close()