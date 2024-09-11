def isPrime(n):
    if(n<=1):
        return 0
    elif(n<4):  
        return 1
    elif(n%2==0): 
        return 0
    elif(n<9):   
        return 1
    elif(n%3==0):
        return 0

    f=5
    r=int(n**0.5)
    while(f<=r):
        if(n%f==0): 
            return 0
        if(n%(f+2)==0):
            return 0
        f=f+6

    return 1

n=int(input())
for i in range(1, 1024):
    if isPrime(i) == 1:
        print(i)