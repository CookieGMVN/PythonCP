n = int(input())
arr = []
for i in range(0, n):
    arr.append(int(input()))
t=0
for i in arr:
    if i%2==0:
        t+=i
print(t)