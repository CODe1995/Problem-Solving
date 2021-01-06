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
n = ii()
field = list()
root = [-1,-1]
def bfs():
    q = deque([[root[0],root[1]]])
    visited = [[root[0],root[1]]]
    answer = 0

    shark_size = 2 # 초기 상어의 크기
    shark_feed = 0 # 상어가 먹은 먹이의 수
    shark_time = 0 # 상어가 움직인 시간(칸당 1 증가)

    eat_flag = False # 먹이를 먹었는지 체크
    # 먹이를 먹었다는 뜻은 가장 위 또는 좌측에 있는 먹이를 먹었으므로
    # 더 이상 반복문(for _ in range(qSize))을 돌릴 필요가 없다는 뜻이다.
    # 해당 반복문을 break하기 위한 용도로 쓰인다.

    while q:
        # 위쪽이 우선, 그 다음 왼쪽이 우선 정렬되어야 하므로
        # y좌표(k[1])를 우선 정렬후 x좌표(k[0])를 기준으로 정렬한다.
        if q:q = deque(sorted(q,key=lambda k:[k[1],k[0]]))
        
        qSize = len(q)
        for _ in range(qSize):
            x,y = q.popleft()
            
            #먹을 수 있는 범위
            if 0<field[y][x]<shark_size:

                field[y][x] = 0 #먹이를 먹었으므로 0으로 변경
                shark_feed+=1   #먹은 먹이 수 증가
                if shark_feed == shark_size:#크기 증가
                    shark_size+=1
                    shark_feed=0
                # 먹이를 먹었으므로 새로운 탐색을 해야한다.
                # 그래서 dq와 visited를 초기화 해준다.
                q=deque()
                visited = [[x,y]]
                answer = shark_time
                eat_flag=True

            for dx,dy in direction:
                nx,ny = x+dx,y+dy

                # 필드 벗어나는 범위 체크, 방문 여부 체크
                if 0<=nx<n and 0<=ny<n and not [nx,ny] in visited:
                    # 이동 가능한 범위
                    if field[ny][nx]<=shark_size:
                        q.append([nx,ny])
                        visited.append([nx,ny])
            
            if eat_flag:
                eat_flag=False
                break
        shark_time+=1
    return answer

# 필드를 입력받고
# 동시에 상어의 위치를 찾고 저장한다.
for i in range(n):
    tmp = lmii()
    field.append(tmp)
    if [-1,-1]==root:
        for j in range(n):
            if tmp[j]==9:
                # 상어를 찾았다면 0으로 초기화 해주고
                # 위치를 root에 등록해 준다.
                root=[j,i]                
                field[i][j]=0    
print(bfs())
# 소스코드 https://dailyheumsi.tistory.com/59 참고