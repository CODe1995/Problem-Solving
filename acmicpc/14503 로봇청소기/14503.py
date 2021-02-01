# 210201 3:33pm ~ 
import sys
from collections import deque
input = sys.stdin.readline
direction = [[0,-1],[1,0],[0,1],[-1,0]]#북동남서
N,M = map(int,input().strip().split())
r,c,d = map(int,input().strip().split())
field = [list(map(int,input().strip().split())) for _ in range(N)]
answer = 0
dq = deque([[c,r,d]])
while dq:
    x,y,d = dq.popleft()
    if field[y][x]==0:#현재위치 청소
        field[y][x]=2
        answer+=1
    #북 > 서 > 남 > 동 > 북 순으로 무한 루틴
    for i in range(4):
        d-=1
        if d==-1:d=3
        nx,ny = x+direction[d][0],y+direction[d][1]
        if 0<=nx<M and 0<=ny<N and field[ny][nx]==0:
            dq.append([nx,ny,d])
            break
    else:#네방향 모두 탐색해도 없다면
        #후방을 바라보는 좌표 반전 1-> -1, -1 -> 1
        if d > 1: f=d-2
        else:f=d+2
        nx,ny = x+direction[f][0],y+direction[f][1]
        
        if 0<=nx<M and 0<=ny<N and field[ny][nx] != 1:#벽아니면
            dq.append([nx,ny,d])
        else:#벽이거나 좌표 벗어나면
            print(answer)
            sys.exit()