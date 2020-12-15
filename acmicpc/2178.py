def bfs(maze,start,goal):
    N = goal[0]
    M = goal[1]
    visited = [[0]*(M+1) for _ in range(N+1)] #방문한 2중 배열을 M*N 크기만큼 생성
    visited[0][0] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    #우 좌 하 상
    # visited[0][0]=1
    next_q = []
    next_q.append(start)
    while next_q:
        bx,by = next_q.pop(0)
        if bx==N and by==M:            
            return visited[bx][by]
        for i in range(4):
            ax = bx+dx[i]
            ay = by+dy[i]
            #MxN 크기 외에 못벗어나게 설정, 방문하지 않은 곳이어야하고, 갈 수 있는 길이어야한다.
            if ax>=0 and ay>=0 and ax<=N and ay<=M and visited[ax][ay]==0 and maze[ax][ay]==1:
                visited[ax][ay] = visited[bx][by] + 1   #이전 거리보다 +1 증가한다
                next_q.append((ax,ay))

N,M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int,input())))
start = (0,0)
goal = (N-1,M-1)
print(bfs(maze,start,goal))
# print(maze)

