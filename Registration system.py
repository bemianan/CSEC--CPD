n=int(input())
names={}
for _ in range(n):
    name=input()
    if name not in names:
        names[name]=1
        print("OK")
    else:
        print(f"{name}{names[name]}")
        names[name]+=1
