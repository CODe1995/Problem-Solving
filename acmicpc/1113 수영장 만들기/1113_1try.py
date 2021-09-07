import copy
N,M = map(int,input().split())
field = [list(map(int,list(input()))) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
direction = [[0,1],[1,0],[-1,0],[0,-1]]
maxheight = 0   #최대 높이
answer = 0
def getHighest():
    global maxheight
    highest = []    #높이가 가장 높은 곳의 좌표들을 반환
    for i in range(N):
        for j in range(M):
            if field[i][j]>maxheight:#높이 갱신
                maxheight = field[i][j]
                highest = [[j,i]]
            elif field[i][j]==maxheight:
                highest.append([j,i])#동일 높이 추가
            #낮으면 무시
    return highest

def outOfPositionCheck(x,y):
    if 0<=x<M and 0<=y<N:
        return True #유효한 범위
    return False #밖으로 나간 경우

def landCheck(x,y):
    if 0==x or 0==y or M-1==x or N-1==y:#땅과 붙어있다면
        return True    
    return False

#x,y 좌표와 물이 흘러들어온 곳의 높이
def dfs(x,y):    
    global answer
    visited[y][x] = 1
    min_height = maxheight
    global_land_check = landCheck(x,y)
    for dx,dy in direction:#4방으로 물이 흐른다 
        nx,ny = dx+x,dy+y
        
        if not outOfPositionCheck(nx,ny):
            continue#외곽이면
        if visited[ny][nx]!=0:#방문?
            if visited[ny][nx]==-1:#땅과 닿아 높이 계산이 의미 없는경우?
                min_height=-1
                visited[y][x]=-1#나도 -1처리
            # continue            
        if field[y][x] >= field[ny][nx]:#물이 흘러갈 수 있는 방향이라면, 방문 안했다면            
            section_height = dfs(nx,ny) #현재 구역에서 최대 높이
            if min_height > section_height:
                min_height = section_height
        else:#물이 막힌다? = 물이 고일 수 있다
            if min_height>field[ny][nx]:#더 작은 높이가 있다면?
                min_height = field[ny][nx]
    
    #자기 자신이 땅과 붙어 있는경우
    if global_land_check:
        visited[y][x]=-1#나도 -1처리
        return -1
    #연결된 땅이 땅과 붙어 있는 경우
    elif min_height==-1:
        visited[y][x]=-1#나도 -1처리
        return min_height
    #그렇지 않은 경우
    else:
        answer += min_height - field[y][x]  #물이 채워질 수 있는 양    
        return min_height

def solution():
    #1. 물은 반드시 높은곳에서 낮은곳으로 흐른다 = 가장 높은 높이에서 물을 흘려보낸다
    highest = getHighest()  #최고 높이를 가져옴

    # for hx,hy in highest:
    for hy in range(N):
        for hx in range(M):
            if visited[hy][hx]==0:
                dfs(hx,hy)
    print(answer)

solution()