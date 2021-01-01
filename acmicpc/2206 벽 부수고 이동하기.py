##########################################################
import sys
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(input().rstrip())
def ips():return ip().split()
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
from collections import deque
direction = [[0,1],[1,0],[-1,0],[0,-1]]
h,w = mii()
field = list()
for _ in range(h):
    field.append(lip())

def bfs():
    q = deque()
    visited = [[[0]*2 for _ in range(w)] for _ in range(h)]
    visited[0][0][0]+=1 #첫 시작점은 1
    #X, Y, 벽 부순 횟수, 방문지
    q.append([0,0,0])
    while q:
        x,y,broken=q.popleft()
        if x==w-1 and y==h-1:
            return visited[y][x][broken]
        for dx,dy in direction:
            nx,ny = dx+x,dy+y
            if 0<=nx<w and 0<=ny<h:
                if visited[ny][nx][broken]==0 and field[ny][nx]=='0':#아직 방문 안했고, 0
                    visited[ny][nx][broken]=visited[y][x][broken]+1
                    q.append([nx,ny,broken])
                elif visited[ny][nx][broken]==0 and field[ny][nx]=='1' and broken==0: #아직 방문 안했고, 1, 벽 안부쉈다면
                    visited[ny][nx][broken+1]=visited[y][x][broken]+1
                    q.append([nx,ny,broken+1])
    return -1
res = bfs()
if res:print(res)
else:print(-1)