import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
field = [list(list(input().strip())) for _ in range(N)]
Apos = list(map(int, input().split()))[::-1]
Bpos = list(map(int, input().split()))[::-1]
Cpos = list(map(int, input().split()))[::-1]
Afootprint = [[0]*M for _ in range(N)]
Bfootprint = [[0]*M for _ in range(N)]
Cfootprint = [[0]*M for _ in range(N)]
direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def bfs(POS):
    x,y = POS[0]-1, POS[1]-1
    footprint = [[0]*M for _ in range(N)]
    dq = deque()
    dq.append([x, y])
    time = 1
    footprint[y][x] = time    
    while dq:
        size = len(dq)
        time+=1
        for _ in range(size):
            cx, cy = dq.popleft()
            for dx, dy in direction:
                nx, ny = cx+dx, cy+dy
                if not (0 <= nx < M and 0 <= ny < N):
                    continue
                if field[ny][nx]=='0' and footprint[ny][nx] == 0:
                    footprint[ny][nx] = time
                    dq.append([nx, ny])
    return footprint

Afootprint = bfs(Apos)
Bfootprint = bfs(Bpos)
Cfootprint = bfs(Cpos)

mintime = M*N
cnt = 0
for i in range(N):
    for j in range(M):
        if field[i][j]==1:continue
        if min(Afootprint[i][j],Bfootprint[i][j],Cfootprint[i][j])==0:continue
        current_maxtime = max(Afootprint[i][j],Bfootprint[i][j],Cfootprint[i][j])-1
        if mintime > current_maxtime:
            mintime = current_maxtime
            cnt = 1
        elif mintime == current_maxtime:
            cnt+=1
if mintime != M*N:
    print(mintime)
    print(cnt)
else:
    print(-1)

