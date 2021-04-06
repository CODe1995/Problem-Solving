import sys
input = sys.stdin.readline
sys.setrecursionlimit(250001)
N,M = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]
direction = [[0,1],[1,0],[-1,0],[0,-1]]
dp = [[-1]*M for _ in range(N)]

def dfs(x,y):
    if [x,y]==[0,0]:
        return 1#끝까지 닿았따
    if dp[y][x]==-1:#방문체크
        dp[y][x]=0
        for dx,dy in direction:
            nx = x+dx
            ny = y+dy
            if 0<=nx<M and 0<=ny<N and field[ny][nx]>field[y][x]:
                dp[y][x]+=dfs(nx,ny)
    return dp[y][x]
print(dfs(M-1,N-1))