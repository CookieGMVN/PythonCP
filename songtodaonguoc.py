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

inp = input()
p = int(inp.split()[0])
q = int(inp.split()[1])

for i in range(p, q+1):
    reversedNumList = list(str(i))
    reversedNumList.reverse()
    reversedNum = int("".join(reversedNumList))
    
    if (ktnt(reversedNum) == True):
        print(i)