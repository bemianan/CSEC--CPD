matrix=[]
for i in range(5):
    matrix.append(list(map(int,input().split())))
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            row=i+1
            col=j+1
            break
if row<3:
    mn_row=3-row
else:
    mn_row=row-3
if col<3:
    mn_col=3-col
else:
    mn_col=col-3
print(mn_row + mn_col)
