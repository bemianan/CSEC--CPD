t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cnt=0
    freq={}
    for i in range(n):
        key=a[i]-i
        cnt+=freq.get(key,0)
        freq[key]=freq.get(key,0)+1
    print(cnt)
