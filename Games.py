n=int(input())
h=[]
g=[]
count=0
for i in range(n):
    hi, gi=map(int,input().split())
    h.append(hi)
    g.append(gi)
for i in h:
    for j in g:
        if i==j:
            count+=1
print(count)
