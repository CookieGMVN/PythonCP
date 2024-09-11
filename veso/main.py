fi=open("vs.inp")
fo=open("vs.out", "w")

lines=fi.readlines()
n=int(lines[0])
maso=list(map(int, lines[1].split()))

for i in range(3, len(lines)):
    kq=int(lines[i])
    fo.write(f"{maso.count(kq)}\n")

fo.close()
fi.close()