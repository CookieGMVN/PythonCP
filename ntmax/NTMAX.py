def ktnt(n):
    if (n<=1):
        return False
    elif n<4:
        return False
    elif (n%3==0 or n%2==0):
        return False
    d=5
    while d<=int((n**0.5))+2:
        if n%d==0 or n%(d+2)==0:
            return False
        else:
            d+=6
    return True

fi=open("NTMAX.INP")
fo=open("NTMAX.OUT", "w")
xau=fi.readline()
xau+=" "
fi.close()
numeric_range=range(48, 58)
current_num=""
max_nto=0
sokt=0
for char in xau:
    if ord(char) in numeric_range:
        sokt+=1
        current_num += char
    else:
        if current_num!="":
            if ktnt(int(current_num)) == True and int(current_num) > max_nto:
                max_nto=int(current_num)
        current_num=""
fo.write(f"{sokt}\n{max_nto}")
fo.close()