lmw, bbw = map(int,input().split())
years=0
while lmw <= bbw:
    years += 1
    lmw*=3
    bbw*=2
print(years)
