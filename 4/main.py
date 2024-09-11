fi=open("DATA.INP")
fo=open("DATA.OUT", "w")

inp=fi.readlines()
arr=list(map(int, inp[1].split()))
increasing_list=[]
increased_list=[]
prev=arr[0]
for i in range(1, len(arr)):
    if prev < arr[i]:
        if len(increasing_list) == 0:
            increasing_list.append(prev)
        increasing_list.append(arr[i])
        if len(increased_list) < len(increasing_list):
            increased_list = increasing_list
    else:
        increasing_list=[] 
    prev=arr[i]       

fo.write(str(len(increased_list)))
fi.close()
fo.close()