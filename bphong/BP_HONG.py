def isRightOrder(src: str, dest: str):
    dest_formatted=""
    for char in dest:
        if char in src and (char in dest_formatted==False or src.count(char)>dest_formatted.count(char)):
            dest_formatted+=char
    if dest_formatted==src:
        return "YES"
    else:
        return "NO"

def solve(src: str, dest: str):
    if src==dest:
        return "YES"
    else:
        for i in src:
            if dest.count(i)<src.count(i):
                return "NO"
        return isRightOrder(src, dest)

fi=open("BP_HONG.INP")
fo=open("BP_HONG.OUT", "w")
n=int(fi.readline())
data=fi.readlines()
final=""
for i in range(0, n*2, 2):
    final+=f"{solve(data[i].strip(), data[i+1].strip())}\n"
fo.write(final.strip())
fo.close()