import sys, heapq
input = sys.stdin.readline
M,N = map(int,input().split())
field = [list(map(int,list(input().strip()))) for _ in range(N)]
INF = 10e9
dist = [[INF]*M for _ in range(N)]
direction = [[0,1],[1,0],[-1,0],[0,-1]]
pq = []
heapq.heappush(pq,[0,0,0])
dist[0][0]=0

while pq:
    d,x,y = heapq.heappop(pq)
    if x==M-1 and y==N-1:
        break
    if d>dist[y][x]:continue
    for dx,dy in direction:
        nx = x+dx
        ny = y+dy
        if 0<=nx<M and 0<=ny<N:
            if dist[ny][nx]>dist[y][x]+field[ny][nx]:
                dist[ny][nx]=dist[y][x]+field[ny][nx]
                heapq.heappush(pq,[dist[ny][nx],nx,ny])
print(dist[N-1][M-1])