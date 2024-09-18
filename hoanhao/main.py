fi=open("hoanhao.inp")
fo=open("hoanhao.out", "w")

n=int(fi.readline())
t=0

for i in range(1, int(n**.5) + 2):
    if n%i==0:
        t+=i

if t==n:
    fo.write(f"{n} là số hoàn hảo")
else:
    fo.write(f"{n} không là số hoàn hảo")

fi.close()
fo.close()