fi=open("DATA.INP")
fo=open("DATA.OUT", "w")

inp=fi.readlines()
arr=list(map(int, inp[1].split()))
st=set(arr)
data={}

for i in st:
    data.update({ i: arr.count(i) })

data_values=set(list(data.values()))
max_value=max(data_values)

for i in data:
    if data.get(i) == max_value:
        fo.write(f"Giá trị lớn nhất: {i}\nSố lần xuất hiện: {max_value}\n\n")

fi.close()
fo.close()