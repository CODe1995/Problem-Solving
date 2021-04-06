import sys
input = sys.stdin.readline
sys.setrecursionlimit(250001)
N = int(input())
field = [list(map(int,input().split())) for _ in range(N)]
direction = [[0,1],[1,0],[-1,0],[0,-1]]
dp = [[-1]*N for _ in range(N)]
answer = 0
def dfs(x,y):
    global answer
    if dp[y][x]==-1:#방문체크
        dp[y][x]=1
        for dx,dy in direction:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<N and field[ny][nx]>field[y][x]:
                dp[y][x]=max(dp[y][x],dfs(nx,ny)+1)
            answer = max(answer,dp[y][x])
    return dp[y][x]

for i in range(N):
    for j in range(N):
        if dp[i][j]==-1:
            dfs(j,i)
print(answer)