s=input()
is_low=0
is_upp=0
for i in s:
    if i.islower():
        is_low+=1
    else:
        is_upp+=1
if is_low>=is_upp:
    print(s.lower())
else:
    print(s.upper())
