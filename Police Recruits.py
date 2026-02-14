n=int(input())
ints=list(map(int,input().split()))
crm=0
pl=0
for i in range(n):
    if ints[i]>0:
        pl+=ints[i]
    else:
        if pl>0:
            pl-=1
        else:
            crm+=1
print(crm)
