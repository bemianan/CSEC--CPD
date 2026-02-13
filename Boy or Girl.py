from collections import defaultdict
string=input()
n=len(string)
freq_dic= defaultdict(int)
for i in range(n):
    freq_dic[string[i]]+=1
if len(freq_dic)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
