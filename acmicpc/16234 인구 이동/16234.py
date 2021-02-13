import sys
input = sys.stdin.readline
from collections import deque
direction = [[0,1],[1,0],[-1,0],[0,-1]]
N,L,R = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]
visited = list()
def bfs(x,y):
    fsum = field[y][x] #탐색한 국가들의 인구 합
    fcnt = 1 #탐색한 국가들의 갯수
    dq = deque([[x,y]])
    current_visit = deque([[x,y]])
    visited[y][x]=1
    while dq:
        x,y = dq.popleft()
        for dx,dy in direction:
            nx,ny = dx+x, dy+y
            if 0<=nx<N and 0<=ny<N and visited[ny][nx]==0 and L<=abs(field[y][x]-field[ny][nx])<=R:
                visited[ny][nx]=1   #방문한 국가는 체크
                dq.append([nx,ny])
                current_visit.append([nx,ny])
                fsum+=field[ny][nx]
                fcnt+=1
    
    if fcnt==1: #인구이동한 국가가 하나라면(없다면)
        return False
    else: 
        while current_visit:#인구이동을 했던 나라에만 값 부여
            x,y = current_visit.popleft()
            field[y][x] = fsum//fcnt    #인구이동
        return True#인구이동을 했다면
    
answer=0
while True:
    result = False
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]:continue
            if bfs(j,i):
                result = True
    if result:
        answer+=1
        # print('==인구이동==============')
        # for c in field:
        #     print(c)        
    else:break#더 이상 돌아도 인구이동이 없는 경우 break
print(answer)