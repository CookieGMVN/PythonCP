def ktnt(n):
    if n<=1:
        return False
    elif n<4:
        return True
    elif n%2==0 or n%3==0:
        return False
    d=5
    while d<=int(n**.5) + 2:
        if n%d==0 or n%(d+2)==0:
            return False
        else:
            d+=6
    return True

n=1000000000
for i in range(1,n+1):
    ktnt(i)