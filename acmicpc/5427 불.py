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

t = ii()
for _ in range(t):
    fire = list()#불위치
    sg = [-1,-1]#상근이위치
    field = list()
    width, height = mii()
    for h in range(height):
        tmp = lip()
        field.append(tmp)
        for w in range(width):
            if tmp[w]=='*':#불위치
                fire.append([w,h])
            elif tmp[w]=='@':#상근이위치
                field[h][w]='.'
                sg=[w,h]              

    def bfs():
        global fire
        q= deque([[sg[0],sg[1]]])    
        visited = [[0]*width for _ in range(height)]#0미방,1방문
        while q:
            #상근이 먼저 움직여!
            lenq = len(q)
            for _ in range(lenq):
                x,y = q.popleft()
                if x==0 or x==width-1 or y==0 or y==height-1:
                    return visited[y][x]+1
                for dx,dy in direction:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<width and 0<=ny<height and visited[ny][nx]==0:
                        if field[ny][nx]=='.':
                            q.append([nx,ny])
                            visited[ny][nx]=visited[y][x]+1
            #불 움직여
            lenf = len(fire)
            tmp = list()
            for i in range(lenf):
                x,y = fire[i]
                for dx,dy in direction:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<width and 0<=ny<height:
                        if field[ny][nx]=='.':
                            field[ny][nx]='*'
                            tmp.append([nx,ny])
            fire=tmp
        return 'IMPOSSIBLE'
    print(bfs())