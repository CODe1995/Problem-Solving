# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위
N,M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int,input())))
start = (0,0)
goal = (N-1,M-1)
# print(maze)
visited = [[0]*N for _ in range(M)] #방문한 2중 배열을 M*N 크기만큼 생성
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

