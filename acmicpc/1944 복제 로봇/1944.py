import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
field = list()
root = [-1,-1]
keys = list()
for i in range(N):
    inp = list(input().strip())

    for j in range(N):
        if inp[j]=='S':
            inp[j]='2'
            root=[j,i]
        elif inp[j]=='K':
            inp[j]=str(len(keys)+3)
            keys.append([len(keys)+3,j,i])
    field.append(inp)
    
graph = list()

direction = [[0,1],[1,0],[-1,0],[0,-1]]
def bfs(x,y):
    dq = deque([[x,y]])    
    visited = [[-1]*N for _ in range(N)]
    visited[y][x]=0
    while dq:
        cur = dq.popleft()
        for dx,dy in direction:
            nx = dx+cur[0]
            ny = dy+cur[1]
            if 0<=nx<N and 0<=ny<N and visited[ny][nx]==-1 and not field[ny][nx]=='1':
                visited[ny][nx]=visited[cur[1]][cur[0]]+1
                if field[ny][nx]>'1':
                    graph.append([int(field[y][x]),int(field[ny][nx]),visited[ny][nx]])#from,to,dist
                dq.append([nx,ny])

bfs(root[0],root[1])
for i in range(len(keys)):
    bfs(keys[i][1],keys[i][2])

parent = [i for i in range(len(keys)+3)]
def getParent(x):
    if x==parent[x]:return x
    parent[x] = getParent(parent[x])
    return parent[x]
def unionParent(a,b):
    a = getParent(a)
    b = getParent(b)
    if a<b:parent[b]=a
    else:parent[a]=b

graph = sorted(graph,key=lambda x:x[2])

answer = 0
for i in range(len(graph)):
    frm,to,d = graph[i]
    frm = getParent(frm)
    to = getParent(to)
    if frm==to:continue
    unionParent(frm,to)
    answer+=d

for i in range(3,len(parent)):
    if parent[i-1]!=parent[i]:
        answer=-1

print(answer)