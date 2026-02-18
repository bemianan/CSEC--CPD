n=int(input())
brd_nums=list(map(int,input().split()))
m=int(input())
for i in range(m):
    xi,yi = map(int,input().split())
    lt_brd=yi-1
    rt_brd=brd_nums[xi-1]-yi
    lt_ind=xi-2
    if lt_ind>=0:
        brd_nums[lt_ind] += lt_brd
    if xi<n:
        brd_nums[xi]+=rt_brd
    brd_nums[xi-1]=0
for i in range(n):
    print(brd_nums[i])
