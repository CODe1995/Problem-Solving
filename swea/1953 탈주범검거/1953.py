###
import sys

sys.stdin = open('C:/Users/code/source/repos/acmicpc/swea/1953 탈주범검거/sample_input.txt')
###

from collections import deque

direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 북동남서
ttype = [
    [],
    [0, 1, 2, 3],
    [0, 2],
    [1, 3],
    [0, 1],
    [1, 2],
    [2, 3],
    [0, 3]
]
T = int(input())
N, M, R, C, L = -1, -1, -1, -1, -1
field = []
visited = []
answer = 0


def init():
    global N, M, R, C, L, field, visited, answer
    N, M, R, C, L = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    answer = 1


def solution():
    global N, M, R, C, L, field, visited, answer
    dq = deque([[C, R]])
    visited[R][C] = 1
    time = 0
    while dq:
        if time == L-1: return
        size = len(dq)
        for i in range(size):
            x, y = dq.popleft()
            for nxt in ttype[field[y][x]]:
                dx, dy = direction[nxt]
                nx, ny = x + dx, y + dy
                if not (0 <= nx < M and 0 <= ny < N):
                    continue
                if visited[ny][nx] == 1:
                    continue
                mirror = (nxt+2)%4
                if not mirror in ttype[field[ny][nx]]:
                    continue
                dq.append([nx, ny])
                visited[ny][nx] = 1
                answer += 1
        time += 1


for tc in range(1, T + 1):
    init()
    solution()
    print('#{} {}'.format(tc, answer))
