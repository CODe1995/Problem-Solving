##########################################################
import sys
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(ip())
def ips():return ip().split()
def ii():return int(input())
def mii():return map(int,ips())
def lmii():return list(mii())
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

def bfs(x,y,size,feed,time):
    q = deque()
    visited = [[[0,0,0] for _ in range(n)] for _ in range(n)]
    eat = set()
    ex,ey=-1,-1
    #x좌표, y좌표, 상어 현재 크기, 먹은 물고기 수, 움직인 수
    q.append([x,y,size,feed,time])    
    while q:
        x,y,size,feed,time = q.popleft()   
        visited[y][x]=[size,feed,time]
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and visited[ny][nx][2]<=time:#범위체크
                if 0<field[ny][nx]<size:#이동&포식
                    q.append([nx,ny,size,feed+1,time+1])
                    visited[ny][nx]=[size,feed+1,visited[y][x][2]+1]
                    eat.add((ny,nx))
                elif (field[ny][nx]==0 or field[ny][nx]==size) and visited[ny][nx][0:1]!=visited[y][x][0:1]:#이동
                    q.append([nx,ny,size,feed,time+1])
                    visited[ny][nx]=[size,feed,visited[y][x][2]+1]     
        if not eat and not q:#아예 못움직이는 상황
            print(visited[ey][ex][2])
            sys.exit()
        elif eat:
            ey,ex = list(eat)[0]
            eat.clear()
            q.clear()
            size,feed = visited[ey][ex][0],visited[ey][ex][1]
            if size==feed:
                size+=1
                feed=0
                visited[ey][ex]=[size,feed,visited[ey][ex][2]]
            field[ey][ex]=0
            q.append([ex,ey,size,feed,visited[ey][ex][2]])        
        
        
    print('done')
    

for i in range(n):
    tmp = lmii()
    field.append(tmp)
    if [-1,-1]==root:
        for j in range(n):
            if tmp[j]==9:#상어위치
                root=[j,i]                
                field[i][j]=0#루트 찾았으니까 초기화
    
print(bfs(root[0],root[1],2,0,0))
