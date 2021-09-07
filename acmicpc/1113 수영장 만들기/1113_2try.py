import sys
from collections import deque
# sys.stdin = open("1113 수영장 만들기/input.txt", "r")
visited = []
field = []
water = []
direction = [[0,1],[1,0],[-1,0],[0,-1]]
N,M=0,0

 
        
def solve():
    global N,M,field,water,visited
    N,M = map(int,input().split())
    field = [list(map(int,list(input()))) for _ in range(N)]
    maxHeight,minHeight = GetMaxMinHeight()  #물이 채워질 수 있는 최대 높이  
    
    # 물을 최대로 채워둔다(가장자리 제외)
    water = [[0]*M for _ in range(N)]
    for i in range(1,N-1):
        for j in range(1,M-1):
            water[i][j] = maxHeight - field[i][j]    

    # 최고 높이에서 한 층씩 제거
    for h in range(maxHeight,minHeight-1,-1):  
        # 방문 기록은 매 높이마다 초기화
        visited = [[0]*M for _ in range(N)] 

        # 벽과 닿은 부분을 제외한 완전 탐색
        for y in range(1,N-1):
            for x in range(1,M-1):
                # 아직 방문 안했고 물이 있는 상태라면? (= 물이 흐를 확률도 있음)
                if not visited[y][x] and water[y][x]:
                    for dx,dy in direction:
                        nx,ny = dx+x,dy+y
                        # 다음 방향으로 물이 흐른다면?
                        if field[y][x]+water[y][x] > field[ny][nx]+water[ny][nx]:
                            DeleteWaterFall(x,y,h)
                            break
    print(getWater())

# 물의 총량 반환
def getWater():    
    global N,M
    ret = 0
    for y in range(1,N-1):
        for x in range(1,M-1):
            ret += water[y][x]
    return ret

# 현재 위치에서 물이 흐르거나 흡수되면 제거
def DeleteWaterFall(x,y,h):
    global N,M,field,water,visited
    dq = deque([[x,y]])
    visited[y][x] = 1

    while dq:
        cx,cy = dq.popleft()
        water[cy][cx]-=1

        for dx,dy in direction:
            nx,ny = cx+dx,cy+dy

            if visited[ny][nx] or 0==nx or 0==ny or M-1==nx or N-1==ny:
                continue

            # 물이 흐를 수 있다면
            if field[ny][nx]+water[ny][nx] == h and water[ny][nx]:
                dq.append([nx,ny])
                visited[ny][nx]=1


# 최대 높이 반환
def GetMaxMinHeight():
    global N,M,field
    maxHeight = 0
    minHeight = 10
    for i in range(N):
        for j in range(M):
            maxHeight = max(field[i][j],maxHeight)
            minHeight = min(field[i][j],minHeight)
    return [maxHeight,minHeight]

# for t in range(3):
#     print('#Testcase : {}'.format(t+1))
solve()   