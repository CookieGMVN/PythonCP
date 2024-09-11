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

n = int(input())
arr = []
for i in range(0, n):
    arr.append(int(input()))
t=0
for i in arr:
    if ktnt(i) == True:
        t+=1
print(t)