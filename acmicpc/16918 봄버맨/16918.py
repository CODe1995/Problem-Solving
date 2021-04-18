import sys
from collections import deque
input = sys.stdin.readline
N,M,T = map(int,input().split())
field = [list(input().strip()) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
direction = [[0,1],[1,0],[-1,0],[0,-1]]
for i in range(N):
    for j in range(M):
        if field[i][j]=='O':
            visited[i][j]=0

def checkBomb(currentTime):
    dq = deque()
    for i in range(N):
        for j in range(M):
            if field[i][j]=='O' and visited[i][j]+3==currentTime:
                dq.append([j,i])
    while dq:
        cur = dq.popleft()
        visited[cur[1]][cur[0]]=-1
        field[cur[1]][cur[0]]='.'
        for dx,dy in direction:
            nx = cur[0]+dx
            ny = cur[1]+dy
            if 0<=nx<M and 0<=ny<N and field[ny][nx]=='O':
                field[ny][nx]='.'
                visited[ny][nx]=-1

def installBomb(currentTime):
    for i in range(N):
        for j in range(M):
            if field[i][j]=='.':
                field[i][j]='O'
                visited[i][j]=currentTime

for currentTime in range(2,T+1):
    installBomb(currentTime)
    checkBomb(currentTime)

for i in range(N):
    for j in range(M):
        print(field[i][j],end='')
    print()