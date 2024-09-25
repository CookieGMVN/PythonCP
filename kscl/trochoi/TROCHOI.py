fi=open("TROCHOI.INP")
fo=open("TROCHOI.OUT", "w")

def getInp():
    return list(map(int, fi.readline().split()))

data=getInp()
n=data[0]
m=data[1]
k=data[2]
data=getInp()
x=data[0]
s=data[1]

support_mins=[]
support_quests=[]
data1=getInp()
data2=getInp()

shortest=m*x

for i in range(0, len(data1)):
    support_mins.append({"reduces": data1[i], "price": data2[i]})

data1=getInp()
data2=getInp()
for i in range(0, len(data1)):
    support_quests.append({"reduces": data1[i], "price": data2[i]})

for support_min in support_mins:
    for support_quest in support_quests:
        if support_min["price"] + support_quest["price"] <= s:
            remaining_time=support_min["reduces"]
            remaining_quests=n-support_quest["reduces"]
            est_time=remaining_quests*remaining_time
            if est_time < shortest:
                shortest = est_time

fo.write(f"{shortest}")