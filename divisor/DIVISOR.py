fi=open("DIVISOR.INP")
fo=open("DIVISOR.OUT", "w")

data=list(map(int, fi.readline().split()))
n=data[0]
k=data[1]
fi.close()
current_step=0
current_num=0
i=1
exs=[]

while current_step < k and i<int(n**.5)+2:
    if n%i==0:
        current_step+=1
        current_num=i
        exs.append(int(n/i))
    i+=1

exs.sort()

if current_step < k:
    if len(exs) >= k-current_step:
        fo.write(f"{exs[int(k-current_step)]}")
    else:
        fo.write("-1")
else:
    fo.write(f"{current_num}")
fo.close()