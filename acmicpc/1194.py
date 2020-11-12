import sys
from collections import deque
input = sys.stdin.readline
direction = [[1,0],[0,1],[-1,0],[0,-1]]
"""
. 빈곳
# 벽
a-f 열쇠    a=97
A-F 대문    A=65
0 현재위치
1 탈출구
"""
"""
3 5
0..a.
#A##.
1....
정답 : 8
열쇠먹고 문따고 가야함
"""
def BFS():
    key_status=0
    cnt = 0
    #좌표값, 키상태, 횟수
    x,y = root
    dq = deque()
    dq.append([x,y,key_status,cnt])
    visited[y][x][key_status]=1
    field[y]=field[y][:x]+'.'+field[y][x+1:] #주인공이 있던 자리는 .으로 대체
    while dq:
        x,y,key_status,cnt = dq.popleft()
        for dx,dy in direction:
            nx = x+dx
            ny = y+dy
            if 0<=nx<M and  0<=ny<N and visited[ny][nx][key_status]==0:    #범위 초과 검토
                _field = field[ny][nx]
                if _field=='#':#벽을 만나면
                    continue
                elif _field=='1':#출구를 만나면
                    return cnt+1
                elif _field=='.':#이동가능한곳       
                    visited[ny][nx][key_status]=1
                    dq.append([nx,ny,key_status,cnt+1]) #이동 했으니까 cnt+1
                elif _field in ['a','b','c','d','e','f']:#키를 만나면
                    _key_status =  key_status | 1 << (ord(_field)-97)
                    visited[ny][nx][_key_status]=1
                    dq.append([nx,ny,_key_status,cnt+1])
                elif _field in ['A','B','C','D','E','F']:#문을 만나면
                    if key_status & 1 <<(ord(_field)-65):#키가 존재하면                        
                        visited[ny][nx][key_status]=1
                        dq.append([nx,ny,key_status,cnt+1])
    return -1

# 세로, 가로
N,M = map(int,input().split())
#키, 가로, 높이
#a~f까지 키를 갖고있는 경우의 수는 총 64개이다.
visited = [[[0]*64 for _ in range(M)] for _ in range(N)]
field = [[[0] for _ in range(M)] for _ in range(N)]
root = []
zero_flag = False
for i in range(N):
    field[i]=input().rstrip()
    if zero_flag==False and '0' in field[i]:
        zero_flag = True
        for j in range(len(field[i])):
            if field[i][j] == '0':
                root = [j,i]   #주인공위치 가로 세로 저장
                break

print(BFS())