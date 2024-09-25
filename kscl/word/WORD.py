fi=open("WORD.INP")
fo=open("WORD.OUT", "w")

ex=fi.readline()
word_nums=int(fi.readline())
word_list=fi.readlines()
final=""

for word in word_list:
    findable=ex.rfind(word.strip())
    if findable == -1:
        final+="No\n"
    else:
        final+="Yes\n"

fo.write(final.strip())