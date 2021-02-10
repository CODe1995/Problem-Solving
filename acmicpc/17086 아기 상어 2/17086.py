import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
field = [list(map(int,input().split())) for i in range(N)]
answer = 0
for y in range(N):
    for x in range(M):
        if field[y][x]==1:continue
        dq = deque([[x,y]])
        visited = [[-1]*M for _ in range(N)]
        visited[y][x]=0
        while dq:
            _x,_y = dq.popleft()
            for dx,dy in [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]:
                nx = _x+dx
                ny = _y+dy
                if 0<=nx<M and 0<=ny<N and visited[ny][nx]==-1:
                    visited[ny][nx]=visited[_y][_x]+1
                    if field[ny][nx]==0:
                        dq.append([nx,ny])
                    else:
                        if answer < visited[ny][nx]:
                            answer = visited[ny][nx]
                        dq = deque()
                        break
print(answer)