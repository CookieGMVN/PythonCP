def ktnt(n):
    if (n<=1):
        return False
    elif n<4:
        return False
    elif (n%3==0 or n%2==0):
        return False
    d=5
    while d<=int((n**0.5))+2:
        if n%d==0 or n%(d+2)==0:
            return False
        else:
            d+=6
    return True

def calc(n):
    nums=list(map(int, list(str(n))))
    t=0
    for num in nums:
       t+=pow(num, 2)
    return ktnt(t)

fi=open("TNT.INP")
fo=open("TNT.OUT", "w")
n=int(fi.readline())
A=list(map(int, fi.readline().strip().split()))
fi.close()
s=0
for num in A:
    if calc(num) == True:
        s+=1
fo.write(str(s))