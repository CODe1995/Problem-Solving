import sys
from collections import deque
input = sys.stdin.readline
direction = [[0,-1],[0,1],[-1,0],[1,0]]#상하좌우
N,M = map(int,input().split())
field = [list(input().strip()) for _ in range(N)]
bluePos = []    #파란구슬 좌표
redPos = []     #빨간구슬 좌표
goalPos = []    #구멍 좌표
visited = [[[[0]*40 for _ in range(40)] for _ in range(40)] for _ in range(40)]
#빨간 구슬과 파란 구슬의 좌표값 저장
for i in range(N):
    for j in range(M):
        if field[i][j] == 'B':
            field[i][j]='.'
            bluePos = [j,i]
        elif field[i][j]=='R':
            field[i][j]='.'
            redPos  = [j,i]
        elif field[i][j]=='O':
            goalPos = [j,i]

def bfs():
    #구슬 좌표 저장
    bx,by,rx,ry = bluePos[0],bluePos[1],redPos[0],redPos[1]
    dq = deque([[1,rx,ry,bx,by]])#횟수, 빨간구슬좌표, 파란구슬좌표
    visited[ry][rx][by][bx]=1
    while dq:
        cnt,rx,ry,bx,by =  dq.popleft()
        for d,[dx,dy] in enumerate(direction):
            nbx,nby = bx,by
            nrx,nry = rx,ry
            while field[nry][nrx] == '.':#벽또는 구멍에 부딪힐 때까지 움직임
                nry+=dy
                nrx+=dx
                if field[nry][nrx]=='#':
                    nry-=dy
                    nrx-=dx
                    break
                elif field[nry][nrx]=='O':
                    break
            while field[nby][nbx] == '.':
                nby+=dy
                nbx+=dx
                if field[nby][nbx]=='#':
                    nby-=dy
                    nbx-=dx
                    break
                elif field[nby][nbx]=='O':
                    break
            if nbx==goalPos[0] and nby==goalPos[1]:#파란구슬이 구멍에 빠졌다면
                continue
            if nry==nby and nrx==nbx:#두 구슬이 겹친다면?
                #원래 좌표와 방향을 확인하고 우선순위 결정
                if d==0:#상:누가 더 위에 있었는가?
                    if by>ry:nby+=1#빨강이 더 위에 있었다면
                    else:nry+=1
                elif d==1:#하:누가 더 아래에 있었는가?
                    if by>ry:nry-=1
                    else:nby-=1
                elif d==2:#좌:누가 더 좌측에 있었는가?
                    if bx<rx:nrx+=1
                    else:nbx+=1
                elif d==3:#우:누가 더 우측에 있었는가?
                    if bx<rx:nbx-=1
                    else: nrx-=1
            if nrx==goalPos[0] and nry==goalPos[1]:
                print(cnt)
                return
            if visited[nry][nrx][nby][nbx]==0 and cnt<40:#빨,파 순                
                visited[nry][nrx][nby][nbx]=1
                dq.append([cnt+1,nrx,nry,nbx,nby])
    print(-1)
bfs()