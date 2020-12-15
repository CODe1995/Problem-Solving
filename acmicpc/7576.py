from collections import deque
width,height = map(int,input().split())
direction = [[1,0],[0,1],[-1,0],[0,-1]]
arr = []
visited=[]
nextq = deque()
for i in range(height):
    arr.append(list(map(int,input().split())))
    visited.append([0]*width)    
    for j in range(width):   #입력과 동시에 토마토 위치를 따로 보관한다.
        if arr[i][j] == 1:
            nextq.append([j,i,0])
            visited[i][j]=1

def bfs():        
    life=0
    while nextq:
        tmx,tmy,life=nextq.popleft()
        arr[tmy][tmx]=1
        for dx,dy in direction:
            nx = tmx+dx
            ny = tmy+dy
            if 0<=nx<width and 0<=ny<height:
                if arr[ny][nx]==0 and visited[ny][nx]==0:
                    nextq.append([nx,ny,life+1])
                    visited[ny][nx]=1    
    for i in range(height):
        if 0 in arr[i]:
            return -1
    return life

print(bfs())