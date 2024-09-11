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

fi=open("DATA.INP")
fo=open("DATA.OUT", "w")

n=int(fi.readline())
nums=list(str(n))

while len(nums)>1:
    if isPrime(int("".join(nums)))==False:
        fo.write(f"False")
        exit()
    nums.pop(-1)

fo.write(f"True")
fi.close()
fo.close()