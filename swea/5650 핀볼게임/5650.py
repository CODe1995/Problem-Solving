###
import sys

sys.stdin = open('C:/Users/code/source/repos/acmicpc/swea/5650 핀볼게임/sample_input.txt')
###
T = int(input())
N = -1
field = []
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
    global N, field, answer, hole
    hole = {}
    answer = 0
    N = int(input())
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
    global N, direction, reflect_direction, field, answer
    initx = x
    inity = y
    points = 0
    while True:
        dx, dy = direction[d]
        x += dx
        y += dy
        if not (0 <= x < N and 0 <= y < N):  # 범위 밖
            d = reflect_direction[5][d]
            points += 1
        elif [initx, inity] == [x, y] or field[y][x] == -1:  # 블랙홀 or 초기위치
            break
        elif 1 <= field[y][x] <= 5:  # 블럭
            d = reflect_direction[field[y][x]][d]
            points += 1
        elif 6 <= field[y][x] <= 10:  # 웜홀
            for hx, hy in hole[field[y][x]]:
                if (hx, hy) != (x, y):  # 반대 구멍
                    x, y = hx, hy
                    break
    answer = max(answer, points)


for tc in range(1, T + 1):
    init()
    for i in range(N):
        for j in range(N):
            if field[i][j] == 0:
                for d in range(4):
                    solution(j, i, d)
    print('#{} {}'.format(tc, answer))
