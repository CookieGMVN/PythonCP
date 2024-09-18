fi=open("sodu.inp")
fo=open("sodu.out", "w")

data=fi.readline().split()
a=int(data[0])
b=int(data[1])
c=int(data[2])

ans=(a**b)%c
fo.write(f"{ans}")
fo.close()
fi.close()
