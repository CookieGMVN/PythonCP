s1=input()
s2=input()
final=""
maxlength=max(list(map(len, [s1, s2])))

c1=0
c2=0
for i in range(0, maxlength):
    if c1<len(s1):
        final += s1[c1]
        c1+=1
    if c2<len(s2):
        final += s2[c2]
        c2+=1
print(final)