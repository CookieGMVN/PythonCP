def ktnt(n):
    if n<=1:
        return False
    elif n<4:
        return True
    elif n%3==0 or n%4==0:
        return False
    d=5
    while d<=int(n**.5)+2:
        if n%d==0 or n%(d+2)==0:
            return False
        else:
            d+=6
    return True

fi=open("sodep.inp")
fo=open("sodep.out", "w")

data=fi.readlines()

for i in range(1, len(data)):
    inp = data[i].split()
    a=int(inp[0])
    b=int(inp[1])
    sd=0

    for i in range(a, b+1):
        uoc=[]
        for d in range(1, i+1):
            if i%d==0:
                uoc.append(d)
        if ktnt(len(uoc)) == True:
            sd+=1
    fo.write(f"{sd}\n")