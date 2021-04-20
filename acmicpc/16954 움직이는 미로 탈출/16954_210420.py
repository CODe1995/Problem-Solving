from collections import deque
MAX = 8
direction = [[0,0],[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,-1],[1,1],[-1,1]]
field=[list(input()) for _ in range(MAX)]
visited=[['.']*MAX for _ in range(MAX)]
dq = deque([[0,7,0]])
answer = 0
while dq:
    cur = dq.popleft()
    visited[cur[1]][cur[0]]='@'
    if cur[1]==0 or cur[2]==7:
        answer=1
        break        
    for dx,dy in direction:
        nx = cur[0]+dx
        ny = cur[1]+dy
        if 0>nx or 0>ny or MAX<=nx or MAX<=ny:continue
        if ny-cur[2]<0:
            dq.clear()
            answer=1
            break
        if field[ny-cur[2]][nx]=='#':continue        
        if field[ny-(cur[2]+1)][nx]=='#':continue        
        dq.append([nx,ny,cur[2]+1])
print(answer)