import sys
from collections import deque
input = sys.stdin.readline
direction = [[0,1],[1,0],[-1,0],[0,-1]]
N,M,K = map(int,input().split())
field = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
def bfs(x,y):
    dq = deque([[x,y]])
    visited[y][x]=1
    cnt = 1
    while dq:
        x,y = dq.popleft()
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if 0<=nx<M and 0<=ny<N and field[ny][nx]==0 and visited[ny][nx]==0:
                visited[ny][nx]=1
                cnt+=1
                dq.append([nx,ny])
    return cnt

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            field[i][j]=1
anscnt = 0
ans = list()
for i in range(N):
    for j in range(M):
        if visited[i][j]==0 and field[i][j]==0:
            ans.append(bfs(j,i))
            anscnt+=1
ans.sort()
print(anscnt)
for x in ans:
    print(x,end=' ')