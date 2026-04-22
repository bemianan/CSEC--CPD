n=int(input())
dic={}
cmax_trc=[]
for _ in range(n):
    name,score=input().split()
    dic[name]=dic.get(name,0)+int(score)
    cmax_trc.append((name,int(score)))
cmax=max(dic.values())
each_rnd={}
for rnd in cmax_trc:
    each_rnd[rnd[0]]=each_rnd.get(rnd[0],0)+rnd[1]
    if dic[rnd[0]]==cmax and each_rnd[rnd[0]]>=cmax:
        print(rnd[0])
        break
