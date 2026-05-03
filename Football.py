n=int(input())
dic={}
for _ in range(n):
    team=input()
    dic[team]=dic.get(team,0)+1
cwin=0
cwtm=''
for team,score in dic.items():
    if score>cwin:
        cwin=score
        cwtm=team
print(cwtm)
 
