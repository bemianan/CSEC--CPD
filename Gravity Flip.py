n=int(input())
no_cubes= list(map(int,input().split()))
no_cubes.sort()
for i in range(n):
    print(no_cubes[i],end=" ")
