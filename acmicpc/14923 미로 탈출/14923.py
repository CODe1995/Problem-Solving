import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
Hy,Hx = map(int,input().split())    #시작위치
Ey,Ex = map(int,input().split())    #탈출위치
Hx-=1; Hy-=1    #시작좌표가 1부터라 보정
Ex-=1; Ey-=1
direction = [[0,1],[1,0],[-1,0],[0,-1]]
visited = [[[0]*M for _ in range(N)] for _ in range(2)]
field = [list(map(int,input().split())) for _ in range(N)]
def bfs():
    if(Hx==Ex and Hy==Ey):#시작부터 출구
        return 0
    dq = deque([[Hx,Hy,0]])#벽부숨 1, 안부숨 0
    d = 1
    while(dq):
        dqSize = len(dq)
        for _ in range(dqSize):
            cur = dq.popleft()
            for dx,dy in direction:
                nx = cur[0]+dx
                ny = cur[1]+dy            
                if(nx==Ex and ny==Ey):#출구발견
                    return d
                if 0<=nx<M and 0<=ny<N and visited[cur[2]][ny][nx]==0:                
                    if field[ny][nx]==1 and cur[2]==0:#벽을 부술 수 있다면
                        dq.append([nx,ny,1])#벽부쉈다는거 체크
                        visited[1][ny][nx]=1
                    elif field[ny][nx]==1 and cur[2]==1:#이미 부쉈다면
                        continue
                    else:
                        visited[cur[2]][ny][nx]=1
                        dq.append([nx,ny,cur[2]])
        d+=1
    return -1
print(bfs())
