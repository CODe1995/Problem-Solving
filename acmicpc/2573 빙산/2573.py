import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
field = [list(map(int,input().strip().split())) for _ in range(N)]
checkMelt = [[0]*M for _ in range(N)]
direction = [[0,1],[1,0],[-1,0],[0,-1]]

def melt():#빙산이 녹음
    #Step1. 주변 물을 파악, field에 반영할 melt 관리
    for i in range(N):
        for j in range(M):
            if field[i][j]==0:continue
            waterCnt = 0
            for dx,dy in direction:
                nx = dx+j
                ny = dy+i
                if 0<=nx<M and 0<=ny<N and field[ny][nx]==0:
                    waterCnt+=1
            checkMelt[i][j] -= field[i][j] if field[i][j]-waterCnt<0 else waterCnt
    
    #Step2. 분석한 melt 값을 field에 직접 반영
    for i in range(N):
        for j in range(M):
            if checkMelt[i][j]==0:continue
            field[i][j]+=checkMelt[i][j]
            checkMelt[i][j]=0

def checkSplit():#빙산의 분리를 체크한다.
    visited = [[0]*M for _ in range(N)]
    iceNumber = 1
    dq = deque()
    for i in range(N):
        for j in range(M):
            if field[i][j]>0 and not visited[i][j]:
                if iceNumber>1:
                    #이미 하나의 빙산 탐색이 끝난 상황에서 또 들어온다면?
                    #빙산이 분리가 되었다는 뜻.
                    return True
                visited[i][j]=1
                dq.append([j,i])
                while dq:
                    cur = dq.popleft()
                    for dx,dy in direction:
                        nx = cur[0]+dx
                        ny = cur[1]+dy
                        if 0<=nx<M and 0<=ny<N and field[ny][nx]>0 and not visited[ny][nx]:#주변에 빙하
                            visited[ny][nx]=1
                            dq.append([nx,ny])
                iceNumber+=1
    return False

answer = 0
if not checkSplit():#시작부터 분리된 경우
    t = 1
    while True:
        melt()
        if checkSplit():
            answer=t
            break
        t+=1
print(answer)