##########################################################
import sys
from collections import deque
direction = [[0,1],[-1,0],[1,0],[0,-1]] #for BFS
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(ip())
def ips():return ip().split()
def ii():return int(input())
def mii():return map(int,ips())
def lmii():return list(mii())
##########################################################
#S 고슴도치
#D 탈출구
#* 물
#X 돌
height,width = mii()
field = list()
water= set()    #물의 좌표를 넣어둔다.
root = [-1,-1]
for i in range(height):
    tmp = lip()
    field.append(tmp)
    for j in range(width):
        if tmp[j]=='*':
            water.add((j,i))
        elif tmp[j]=='S':
            root = [j,i]
            field[i][j]='.'
def bfs():
    q = deque([[root[0],root[1]]])
    visited = [[0]*width for _ in range(height)]
    
    while q:        
        #물을 먼저 채워준다.
        for wx,wy in list(water):
            for dx,dy in direction:
                nx,ny = dx+wx, dy+wy
                if 0<=nx<width and 0<=ny<height and field[ny][nx]=='.':
                    field[ny][nx]='*'
                    water.add((nx,ny))
        lenq = len(q)
        for _ in range(lenq):
            #그 다음 고슴도치가 이동한다.
            x,y = q.popleft()
            for dx,dy in direction:
                nx,ny = x+dx, y+dy
                if 0<=nx<width and 0<=ny<height:
                    if field[ny][nx]=='.':
                        visited[ny][nx]=visited[y][x]+1
                        q.append([nx,ny])
                    elif field[ny][nx]=='D':#종료조건
                        return visited[y][x]+1
    return 'KAKTUS'

print(bfs())