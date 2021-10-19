##
import sys

sys.stdin = open('C:/Users/code/source/repos/acmicpc/swea/1949 등산로조성/sample_input.txt')
##

T = int(input())
N, K = -1, -1
field = []
dp = []
answer = 1
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
maxPosition = []
visited = []


def init():
    global N, K, field, dp, answer, maxPosition
    N, K = map(int, input().split())
    answer = 1
    field = [list(map(int, input().split())) for _ in range(N)]
    maxValue = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] > maxValue:
                maxValue = field[i][j]
                maxPosition = [i * N + j]
            elif field[i][j] == maxValue:
                maxPosition.append(i * N + j)


def solution(depth, x, y, cut: bool):
    global answer, field, K, visited
    visited[y][x] = depth
    if answer < depth:
        answer = depth
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if visited[ny][nx] != 0: continue
        if field[ny][nx] < field[y][x]:  # 안깎음
            solution(depth + 1, nx, ny, cut)
        if field[ny][nx] >= field[y][x] and field[ny][nx] - field[y][x] + 1 <= K and not cut:
            tmp = field[ny][nx]
            field[ny][nx] -= field[ny][nx] - field[y][x] + 1
            solution(depth + 1, nx, ny, True)
            field[ny][nx] = tmp
    visited[y][x] = 0


for tc in range(1, T + 1):
    init()
    for mp in maxPosition:
        x, y = mp % N, mp // N
        visited = [[0] * N for _ in range(N)]
        solution(1, x, y, False)
    print('#{} {}'.format(tc, answer))
