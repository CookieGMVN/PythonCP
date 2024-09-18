fi=open("dulich.inp")
fo=open("dulich.out", "w")

data=fi.readlines()
n=int(data[0].split()[0])
m=int(data[0].split()[1])
routes=[]
final_fees=[0]

for i in range(1, len(data)):
    routes.append(list(map(int, data[i].split())))

def findRoutes(to):
    rts=[]
    for i in routes:
        if i[1] == to:
            rts.append(i)
    return rts

def calcFee(to):
    rts=findRoutes(to)
    for i in rts:
        if i[0] != 1:
            print(i)

fee=0
stage=1
while stage < 