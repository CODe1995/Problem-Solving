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
# 초기 아기 상어 크기 : 2
# 자기보다 작은 크기는 먹을 수 있음
# 같은 크기는 지나갈 수 있음
# 큰 크기는 지나가는 것도 안됌.
# 본인 크기의 물고기 수를 먹으면 크기 증가.
# 거리 결정 순서 : 
#   1. 가장 가까움
#   2. 가장 위
#   3. 가장 왼쪽
from collections import deque
direction = [[0,1],[-1,0],[1,0],[0,-1]]
n = ii()
field = list()
root = [-1,-1]
for i in range(n):
    tmp = lmii()
    if [-1,-1]==root:
        for j in range(n):
            if tmp[j]==9:#상어위치
                root=[j,i]
    field.append(tmp)

def bfs():
    q = deque()
    visited = [[[0]*9 for _ in range(n)] for _ in range(n)]
    #x좌표, y좌표, 상어 현재 크기, 먹은 물고기 수, 움직인 수
    q.append([root[0],root[1],2,0,0])
    while q:
        x,y,size,feed,move = q.popleft()
        if size==feed:size+=1#크기 증가            
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:#범위체크
                if field[ny][nx]<=size:#이동&먹기
                    if field[ny][nx]<size and field[ny][nx]!=0:#먹으면서 이동
                        q.append([nx,ny,size,feed+1,move+1])
                        field[ny][nx]=0#먹었으니까 0으로 초기화
                    else:
                        q.append([nx,ny,size,feed,move+1])
    return move
print(bfs())
