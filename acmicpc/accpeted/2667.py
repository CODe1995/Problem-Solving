n = int(input())
field = []
direction = [[0,1],[1,0],[-1,0],[0,-1]]

for i in range(n):
    field.append(list(map(int,input())))

visited = [[0]*n for _ in range(n)]

def dfs(nx,ny,cnt):
    visited[nx][ny]=1
    for dx,dy in direction:
        tx = nx+dx
        ty = ny+dy
        if tx>=0 and ty>=0 and tx<n and ty<n:
            if visited[tx][ty]==0 and field[tx][ty]==1:
                cnt=dfs(tx,ty,cnt+1)
    return cnt
ans = []
for i in range(n):
    for j in range(n):
        if field[i][j]==1 and visited[i][j]==0:            
            ans.append(dfs(i,j,0)+1)
print(len(ans))
for i in sorted(ans):
    print(i)