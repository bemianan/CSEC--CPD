freq_count=[0]*2
n= int(input())
s= str(input())
for i in range(n):
    if s[i]=='A':
        freq_count[0]+=1
    else:
        freq_count[1]+=1
if freq_count[0]>freq_count[1]:
    print("Anton")
elif freq_count[0]==freq_count[1]:
    print("Friendship")
else:
    print("Danik")
