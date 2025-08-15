n, m, x, y = map(int, input().split(' '))
#在下方继续编写代码
l=[[0 for _ in range(m+1)] for _ in range(n+1)]
a=[-1,-2,-2,-1,1,2,2,1]
b=[2,1,-1,-2,-2,-1,1,2]
for i in range(len(a)):
    if 0<=x+a[i]<=n and 0<=y+b[i]<=m:
        l[x+a[i]][y+b[i]]=-1
l[x][y]=-1
path=[[0 for _ in range(m+1)] for _ in range(n+1)]
path[0][0]=1
for i in range(1,m+1):
    if not l[0][i]:
        path[0][i]=path[0][i-1]
for i in range(1,n+1):
    if not l[i][0]:
        path[i][0]=path[i-1][0]
for i in range(1,n+1):
    for j in range(1,m+1):
        if not l[i][j]:
            path[i][j]=path[i-1][j]+path[i][j-1]
print(path[n][m])
