def timUoc(n):
    uoc=[]
    for i in range(2, int(n**.5)+1):
        if n%i==0:
            uoc.append(i)
            if n // i != i and n // i != n:
                uoc.append(n//i)
    return uoc

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

def solve(m, n):
    if ktnt(m) == True and ktnt(n) == True:
        return "NO"
    tm=sum(timUoc(m))
    tn=sum(timUoc(n))
    print(timUoc(m))
    print(timUoc(n))
    if tm==tn:
        return "YES"
    else:
        return "NO"

fi=open("ANHEM.INP")
fo=open("ANHEM.OUT", "w")
m,n=list(map(int, fi.readline().strip().split()))
fi.close()
fo.write(solve(m, m))
fo.close()