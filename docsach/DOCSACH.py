def solve(page: int, step: int):
    ckt=0
    s=0
    total=int(page/step)
    for i in range(1, 11):
        last_num=int(list(str(step*i))[-1])
        ckt += int(last_num)
    print(ckt)
    for i in range(0, total):
        s+=ckt*(int(total//10))
    return s

fi=open("DOCSACH.INP")
fo=open("DOCSACH.OUT", "w")

q=int(fi.readline())
pages=fi.readlines()
final=""

tasks = []
for i in pages:
    data=list(map(int, i.strip().split()))
    final+=f"{solve(data[0], data[1])}\n"
fo.write(final.strip())