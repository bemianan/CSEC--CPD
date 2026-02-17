y,w=map(int,input().split())
gt=max(y,w)
dt=6-(gt-1)
dt_prob=["0/1","1/6","1/3","1/2","2/3","5/6","1/1"]
print(dt_prob[dt])
