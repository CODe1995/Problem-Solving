import sys
sys.setrecursionlimit(100000)
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
field = list()
icebergs = deque()
for i in range(N):
    field.append(list(map(int,input().strip().split())))
    for j in range(M):
        if field[i][j]>0:#빙산인 경우
            icebergs.append([j,i])

checkMelt = [[0]*M for _ in range(N)]
direction = [[0,1],[1,0],[-1,0],[0,-1]]

def melt():#빙산이 녹음
    #Step1. 주변 물을 파악, field에 반영할 melt 관리
    size = len(icebergs)
    melted = deque()#녹은 빙산
    for i in range(size):
        cur = icebergs.popleft()
        waterCnt = 0
        for dx,dy in direction:
            nx = dx+cur[0]
            ny = dy+cur[1]
            if 0<=nx<M and 0<=ny<N and field[ny][nx]==0:
                waterCnt+=1
        if field[cur[1]][cur[0]]-waterCnt<=0:#녹아 없어진다면?
            melted.append([cur[0],cur[1]])
            checkMelt[cur[1]][cur[0]] -= field[cur[1]][cur[0]] if field[cur[1]][cur[0]]-waterCnt<0 else waterCnt
        else:#바로 녹여도 영향 없는 빙하들
            field[cur[1]][cur[0]]-=waterCnt
            icebergs.append([cur[0],cur[1]])#살아남아 있기때문에 다시 덱에 넣어줌
            
    #Step2. 녹아 없어지는 빙산들 field에 반영
    while melted:
        cur = melted.popleft()
        field[cur[1]][cur[0]]+=checkMelt[cur[1]][cur[0]]
        checkMelt[cur[1]][cur[0]]=0

def dfs(visited,x,y):
    visited[y][x]=1
    for dx,dy in direction:
        nx = x+dx
        ny = y+dy
        if 0<=nx<M and 0<=ny<N and not visited[ny][nx] and field[ny][nx]>0:
            dfs(visited,nx,ny)

def checkSplit():#빙산의 분리를 체크한다.
    visited = [[0]*M for _ in range(N)]
    iceNumber = 1

    for i in range(len(icebergs)):
        x,y = icebergs[i]
        if visited[y][x]:continue#방문체크
        if i>0:#재탐색이 이뤄짐 = 빙하가 분리되어있음
            return True
        visited[y][x]=1
        dfs(visited,x,y)

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