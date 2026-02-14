n= int(input())
nums=list(map(int,input().split()))
sereja=0
dima=0
lt = 0
rt=n-1
turn=True
while lt<=rt:
    if nums[lt]<nums[rt]:
        num=nums[rt]
        rt-=1
    else:
        num=nums[lt]
        lt+=1
    if turn:
        sereja+=num
        turn=False
    else:
        dima+=num
        turn=True
print(sereja,dima)
