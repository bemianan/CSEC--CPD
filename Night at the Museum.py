length=['', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=input()
count=0
init=length.index('a')
for i in range(len(s)):
    let=length.index(s[i])
    count+= min(abs(init-let), 26 -abs(init-let))
    init=let
print(count)
