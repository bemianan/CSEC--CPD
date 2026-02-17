s=input()
t=input()
j=0
count=1
for i in range(len(t)):
    if t[i]==s[j]:
        count+=1
        j+=1
print(count)
