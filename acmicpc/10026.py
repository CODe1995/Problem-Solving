import sys
from collections import deque
sys.setrecursionlimit(100000)
N = int(input())
direction = [[1,0],[0,1],[-1,0],[0,-1]]
arr = []
visited1=[]
visited2=[]
nextq = deque()
for i in range(N):
    arr.append(list(input()))
    visited1.append([0]*N)    
    visited2.append([0]*N)    
cnt = 0

def dfs(x,y,color,visited):
    for dx,dy in direction:
        nx=x+dx
        ny=y+dy
        if 0<=nx<N and 0<=ny<N:
            if arr[ny][nx] in color and visited[ny][nx]==0:
                visited[ny][nx]=1
                dfs(nx,ny,color,visited)

for i in range(N):
    for j in range(N):
        if visited1[i][j]==0:
            visited1[i][j]=1
            dfs(j,i,arr[i][j],visited1)
            cnt+=1
print(cnt,end=' ')
cnt = 0

for i in range(N):
    for j in range(N):
        if visited2[i][j]==0:
            visited2[i][j]=1
            dfs(j,i,['R','G'] if arr[i][j] in ['R','G'] else arr[i][j],visited2)
            cnt+=1
print(cnt)