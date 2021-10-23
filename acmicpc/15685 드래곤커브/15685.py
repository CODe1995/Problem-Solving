import sys

input = sys.stdin.readline
N = int(input())
dragoncurves = [list(map(int, input().split())) for _ in range(N)]
dragonstack = []
direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
field = []


def generate(x, y):
    global dragonstack
    size = len(dragonstack)
    for i in range(size - 1, -1, -1):
        prev = dragonstack[i]
        dir = (prev + 1) % 4  # 다음 방향
        nx, ny = x + direction[dir][0], y + direction[dir][1]  # 끝나는 좌표
        field[ny][nx] = 1
        dragonstack.append(dir)
        x, y = nx, ny
    return [x, y]


def solution():
    global N, dragonstack, field
    field = [[0] * 101 for _ in range(101)]
    for i in range(N):
        dragonstack.clear()
        x, y, d, g = dragoncurves[i]
        field[y][x] = 1
        nx = direction[d][0] + x
        ny = direction[d][1] + y
        field[ny][nx] = 1
        dragonstack.append(d)  # 0세대
        for gen in range(1, g + 1):  # 1~g세대
            nx, ny = generate(nx, ny)
    answer = 0
    for i in range(101 - 1):
        for j in range(101 - 1):
            if field[i][j] + field[i][j + 1] + field[i + 1][j] + field[i + 1][j + 1] == 4:
                answer += 1
    print(answer)


solution()
