import sys
import heapq
input = sys.stdin.readline

INF = 10e9
directions = [[0,1],[1,0],[-1,0],[0,-1]]
cnt = 1
while True:
    N = int(input())
    if N==0:break

    field = [list(map(int,input().strip().split())) for _ in range(N)]
    d = [[INF]*N for _ in range(N)]
    d[0][0] = field[0][0]

    pq = []
    heapq.heappush(pq,[field[0][0],0,0])
    while pq:
        cur = heapq.heappop(pq)
        x = cur[1]
        y = cur[2]
        for direction in directions:
            nx = cur[1] + direction[0]
            ny = cur[2] + direction[1]
            if 0<=nx<N and 0<=ny<N:
                if d[ny][nx] > d[y][x] + field[ny][nx]:
                    d[ny][nx] = d[y][x] + field[ny][nx]
                    heapq.heappush(pq,[d[ny][nx],nx,ny])
    print('Problem {}: {}'.format(cnt,d[-1][-1]))
    cnt+=1