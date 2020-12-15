import sys,copy
from collections import deque

input = sys.stdin.readline
direction = [[0,1],[1,0],[-1,0],[0,-1]]
height,width = map(int,input().split())
field = []
for _ in range(height):
    field.append(list(map(int,input().split())))
virusList=[]
maxval=0
nextq = deque()
visited = [[0]*width for _ in range(height)]

def spreadVirus(cField):
    while nextq:        
        nx,ny = nextq.popleft()
        for dx,dy in direction:
            tx =nx+dx
            ty =ny+dy
            if tx>=0 and tx<width and ty>=0 and ty<height and cField[ty][tx]!=1:
                if cField[ty][tx] == 0 and visited[ty][tx]==0:         
                    cField[ty][tx]=2
                    visited[ty][tx]=1           
                    nextq.append([tx,ty])

def safeArea(cField):
    cnt = 0
    for i in range(height):
        for j in range(width):
            if cField[i][j] == 0:
                cnt+=1
    return cnt

def setWall(start,cnt):
    global maxval,visited
    if cnt == 3:
        copyed = copy.deepcopy(field)
        for vx,vy in virusList:
            nextq.append([vx,vy])
            visited[vy][vx]=1
            spreadVirus(copyed)
            visited = [[0]*width for _ in range(height)]
        maxval = max(maxval,safeArea(copyed))
        return
    for i in range(start, width*height):
        y = (int) (i / width)
        x = (int) (i % width)        
        if field[y][x]==0:
            field[y][x]=1
            setWall(start+1,cnt+1)
            field[y][x]=0

for i in range(height):
    for j in range(width):
        if field[i][j] == 2:
            virusList.append([j,i])

setWall(0,0)
print(maxval)