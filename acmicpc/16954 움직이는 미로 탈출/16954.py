import sys
from collections import deque
field = [list(input()) for _ in range(8)]
# visited = [[0]*8 for _ in range(8)]
direction = [[0,-1],[-1,-1],[1,-1],[1,0],[-1,0],[0,0]]
dq = deque([[0,7]])
while dq:
    x,y = dq.popleft()
    for dx,dy in direction:
        nx,ny = dx+x,dy+y#y값 턴마다 움직임
        if 0<=nx<8 and 0<=ny<8 and field[ny][nx]=='.':
            if y==0:
                print(1)
                sys.exit()            
            if ny==0 or field[ny-1][nx]=='#':continue
            # visited[ny-1][nx] = 1
            dq.append([nx,ny-1])
print(0)