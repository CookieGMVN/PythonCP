fi=open("longchim.inp")
fo=open("longchim.out", "w")

n=int(fi.readline())
lengths=list(map(int, fi.readline().split()))
actual_lengths=list(set(lengths))
lengths_obj=[]

for i in actual_lengths:
    lengths_obj.append({"length": i, "count": lengths.count(i)})

lengths_obj.sort(key=lambda x:x["count"], reverse=True)

final1=""
final2=""
for i in lengths_obj:
    final1 += f"{i['length']} "
    final2 += f"{i['count']} "

fo.write(final1.strip() + "\n" + final2.strip())
fi.close()
fo.close()