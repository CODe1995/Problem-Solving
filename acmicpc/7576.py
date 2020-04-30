from collections import deque
width,height = map(int,input().split())
direction = [[1,0],[0,1],[-1,0],[0,-1]]
arr = []
visited=[]
afarr = []
nextq = deque()
cnt=0
for i in range(height):
    arr.append(list(map(int,input().split())))
    visited.append([0]*width)
    for j in range(width):   #입력과 동시에 토마토 위치를 따로 보관한다.
        if arr[i][j] == 1:
            nextq.append([j,i,0])
            visited[i][j]=1

afarr = arr

def bfs():        
    while nextq:
        tmx,tmy,life=nextq.popleft()
        afarr[tmy][tmx]=1
        for dx,dy in direction:
            nx = tmx+dx
            ny = tmy+dy
            if nx >=0 and ny>=0 and nx<width and ny<height:
                if afarr[ny][nx]==0 and visited[ny][nx]==0:
                    nextq.append([nx,ny,life+1])
                    visited[ny][nx]=1
    pos = True
    for i in range(height):
        for j in range(width):
            if afarr[i][j]==0:
                pos = False
                print(-1)
                break      
    if pos == True:      
        print(life)

bfs()


