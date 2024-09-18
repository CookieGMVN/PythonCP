s=input().split()
d=list(set(s))
data={"c": "", "a": 0}

for i in d:
    if s.count(i) > data["a"]:
        data["a"] = s.count(i)
        data["c"] = i

print(data["c"])