def isPrime(n):
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

fi=open("prime.inp")
fo=open("prime.out", "w")

data=list(map(int, fi.readline().split()))
a=data[0]
b=data[1]
d=0

for i in range(a, b+1):
    chars=list(str(i))
    chars.reverse()
    if  isPrime((int("".join(chars)))) == True:
        d+=1
        
fo.write(str(d))

fi.close()
fo.close()