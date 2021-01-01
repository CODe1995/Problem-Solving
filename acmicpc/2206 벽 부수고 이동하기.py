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
    #X, Y, 벽부순 갯수, 이동거리
    q.append([0,0,0,1])
    while q:
        x,y,broken,move=q.popleft()        
        for dx,dy in direction:
            nx,ny = dx+x,dy+y
            if 0<=nx<w and 0<=ny<h:
                if field[ny][nx]=='0':
                    q.append([nx,ny,broken,move+1])
                elif field[ny][nx]=='1' and broken==0:
                    q.append([nx,ny,broken+1,move+1])                    
                if [nx,ny]==[w-1,h-1]:
                    return move+1

res = bfs()
if res:print(res)
else:print(-1)