import sys
from collections import deque

# sys.stdin = open("C:/Users/code/source/repos/acmicpc/acmicpc/3197 백조의 호수/input.txt")
input = sys.stdin.readline

N, M = 0, 0
field = []
parent = []
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
swan = []
visited = []
nextq = []


def find(x):
    global parent
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True


def bfs(x, y):
    global visited, N, M, direction, field, nextq
    dq = deque()
    dq.append([x, y])
    while dq:
        cur = dq.popleft()
        cx, cy = cur[0], cur[1]
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N:
                if visited[ny][nx]: continue
                visited[ny][nx] = 1
                if field[ny][nx] == '.':
                    union(x + y * M, nx + ny * M)
                    dq.append([nx, ny])
                elif field[ny][nx] == 'X':
                    nextq.append([nx, ny])


def init():
    global N, M, field, parent, swan, visited, nextq
    N, M = map(int, input().split())
    field = [list(input().strip()) for _ in range(N)]
    swan = []
    parent = [i for i in range(N * M + 1)]
    nextq = deque()
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if field[i][j] == 'L':
                swan.append([j, i])
                field[i][j] = '.'
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1: continue
            if field[i][j] == 'X': continue
            bfs(j, i)


def melt():
    global field, nextq, direction, N, M, visited
    dq = deque()
    while nextq:
        cur = nextq.popleft()
        x, y = cur[0], cur[1]
        field[y][x] = '.'
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if field[ny][nx] == '.':
                    union(x + y * M, nx + ny * M)
                if visited[ny][nx]: continue
                visited[ny][nx] = 1
                if field[ny][nx] == 'X':
                    dq.append([nx, ny])
    nextq = dq


def printParents():
    global parent, M
    print('parent---')
    for i in range(N):
        for j in range(M):
            find(j + i * M)
        print(parent[i * M:i * M + M])


# for i in range(3):
#     print('game:', i)
init()
gameRound = 0
#     # printParents()
while True:
    if find(swan[0][0] + swan[0][1] * M) == find(swan[1][0] + swan[1][1] * M):
        print(gameRound)
        break
    melt()
    # printParents()
    gameRound += 1
