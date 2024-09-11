n = int(input())
ans = []

for i in range(2, int(n**.5)+2):
    while n%i==0:
        ans.append(i)
        n=n/i

if n>1:
    ans.append(n)

diffAns = list(set(ans))

final = f""

for i in range(0, len(diffAns)):
    final += f"{diffAns[i]}^{ans.count(diffAns[i])}"
    if (i+1<len(diffAns)):
        final += f" x "

print(final)