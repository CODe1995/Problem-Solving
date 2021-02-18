import sys
input = sys.stdin.readline
N,M = map(int,input().split())
field = [list(input().strip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
def dfs(x,y):
    visited[y][x]=1
    for dx,dy in [[1,-1],[1,0],[1,1]]:
        nx,ny = x+dx,y+dy
        if ny<0 or ny>=N:continue
        if nx==M-1:
            visited[ny][nx]=1
            return 1
        if visited[ny][nx]==0 and field[ny][nx]=='.':
            if dfs(nx,ny):return 1
    return 0
answer=0
for i in range(N):
    answer+=dfs(0,i)
print(answer)