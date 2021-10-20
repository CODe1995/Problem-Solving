###
import sys

sys.stdin = open('C:/Users/code/source/repos/acmicpc/swea/5650 핀볼게임/sample_input.txt')
###
T = int(input())
N = -1
field = []
visited = []  # 방향기록 0000 비트마스킹
dp = []  # 각 위치별 점수 기록
hole = dict()  # 구멍 관계
answer = -1
direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # 상하좌우
reflect_direction = [
    [],
    [1, 3, 0, 2],
    [3, 0, 1, 2],
    [2, 0, 3, 1],
    [1, 2, 3, 0],
    [1, 0, 3, 2]
]


def init():
    global N, dp, visited, field, answer
    answer = 0
    N = int(input())
    dp = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    field = []
    for i in range(N):
        inp = list(map(int, input().split()))
        for j in range(N):
            if inp[j] >= 6:  # 웜홀
                if inp[j] in hole:
                    hole[inp[j]].append([j, i])
                else:
                    hole[inp[j]] = [[j, i]]
        field.append(inp)


def solution(x, y, d):
    global N, direction, reflect_direction
    initx = x
    inity = y
    initd = d
    points = 0
    gamecnt = 0
    while True:
        # 장외는 미리 처리한다
        if gamecnt != 0 and [initx, inity, initd] == [x, y, d]:  # 방문지로 돌아온 경우
            return points
        if visited[y][x] & (1 << d):  # 이미 계산된 경우
            return dp[y][x][d] + points
        gamecnt += 1
        visited[y][x] |= 1 << d  # 방문처리
        dp[y][x][d] = max(points, dp[y][x][d])
        if 1 <= field[y][x] <= 5:  # 벽을 만난 경우
            d = reflect_direction[field[y][x]][d]  # 방향 변환
            points += 1
        elif field[y][x] == 0:  # 그냥 이동
            pass
        elif field[y][x] == -1:  # 블랙홀
            return points
        elif 6 <= field[y][x] <= 10:  # 웜홀
            for dx, dy in hole[field[y][x]]:
                if [dx, dy] != [x, y]:
                    x, y = dx, dy
            continue
        nx, ny = x + direction[d][0], y + direction[d][1]
        if not (0 <= nx < N and 0 <= ny < N):  # 장외라면?
            d = reflect_direction[5][d]  # 방향 변환
            points += 1
            # 좌표는 그대로
        else:
            x, y = nx, ny


for tc in range(1, T + 1):
    init()
    for i in range(N):
        for j in range(N):
            if field[i][j] == 0:
                for d in range(4):
                    if visited[i][j] & (1 << d):  # 갔던 방향은 패스
                        continue
                    answer = max(answer, solution(j, i, d))
    print('#{} {}'.format(tc, answer))
