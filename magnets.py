n=int(input())
res=[]
for i in range(n):
    mg=input()
    p1=int(mg[0])
    p2=int(mg[1])
    if len(res) == 0 or res[-1][-1]==p1:
        res.append([p1,p2])
    else:
        res[-1].append(p1)
        res[-1].append(p2)
print(len(res))
