n=int(input())

is_prime=[True]*n
is_prime[0]=False
for i in range(2, int(n**.5)+1):
    d=i*i
    while d<=n+1:
        is_prime[d-1]=False
        d=d*i

print(is_prime[n-1])