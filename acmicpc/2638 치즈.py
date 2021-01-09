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

height,width = mii()
field = list()
moveQ = deque()
chzcnt = 0
#치즈 개수 세면서 동시에 삽입
for _ in range(height):
    tmp = lmii()
    chzcnt+=sum(tmp)
    field.append(tmp)

def bfs():
    global chzcnt
    visited = [[-1]*width for _ in range(height)]
    visited[0][0]=0
    q = deque([[0,0]])
    while q:
        x,y = q.popleft()
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if 0<=nx<width and 0<=ny<height:
                if visited[ny][nx]==-1 and field[ny][nx]==0:#첫방문,공기층
                    visited[ny][nx]=0
                    q.append([nx,ny])
                elif field[ny][nx]==1:
                    visited[ny][nx]+=1#0,1
                    if visited[ny][nx]==1:
                        chzcnt-=1
                        field[ny][nx]=0
                        visited[ny][nx]=0
cnt=0
while chzcnt:
    bfs()
    cnt+=1
print(cnt)