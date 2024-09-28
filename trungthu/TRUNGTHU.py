fi=open("TRUNGTHU.INP")
fo=open("TRUNGTHU.OUT", "w")
n=int(fi.readline())
data="".join(fi.readlines())+"\n"
char_range=range(48, 58)
chars=[]
current=""
current_value=0
for c in data:
    if c!= "\n":
        current+=c
    if c=="\n":
        chars.append({"content": current, "value": current_value})
        current=""
        current_value=0
    if ord(c) in char_range:
        current_value+=int(c)
chars.sort(key=lambda x:x["value"])
fo.write("\n".join([item["content"] for item in chars]))