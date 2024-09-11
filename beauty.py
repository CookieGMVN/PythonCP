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

def beautyCheck(n):
    nums = list(str(n))
    if len(nums) <= 1:
        return False
    t=0
    for i in nums:
        t+=int(i)**2
    if ktnt(t):
        return True
    else:
        return False

def findBeauty(n):
    i=11
    index=1
    while index<n:
        i+=1
        if beautyCheck(i) == True:
            index+=1
    return i

n=int(input())
print(findBeauty(n))