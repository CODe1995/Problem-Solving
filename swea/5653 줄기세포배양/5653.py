####
# import sys
# sys.stdin = open('C:/Users/code/source/repos/acmicpc/swea/5653 줄기세포배양/sample_input.txt')
####
from collections import deque

T = int(input())
N, M, K = -1, -1, -1
field = []
inactive = deque()
active = deque()
used = deque()
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def init():
    global N, M, K, field, inactive, active, used
    inactive = deque()
    active = deque()
    used = deque()
    N, M, K = map(int, input().split())
    field = [[0] * (M + 2 * K) for _ in range(N + 2 * K)]
    for i in range(N):
        inp = list(map(int, input().split()))
        for j in range(M):
            if inp[j] == 0: continue
            field[i + K][j + K] = inp[j]
            inactive.append([j+K, i+K, 0, inp[j]])


def spread(current_time: int):
    global inactive, active, used, direction, field

    # 1. 활성화 체크
    active = deque(sorted(active, key=lambda x: (-x[3])))
    while active:
        cur = active.popleft()
        for dx, dy in direction:
            nx, ny = dx + cur[0], dy + cur[1]
            if not (0 <= nx < M + 2 * K and 0 <= ny < N + 2 * K): continue
            if field[ny][nx] != 0 or field[ny][nx] >= cur[3]: continue
            field[ny][nx] = cur[3]
            inactive.append([nx, ny, current_time, cur[3]])
        # 2 이상은 used로 보내기, 1의 경우 바로 폐기하기
        if cur[3] == 1: continue
        used.append(cur)

    # 2. 비활 -> 활성화
    inactive = deque(sorted(inactive, key=lambda x: (x[2] + x[3], -x[3])))
    while inactive:
        if not inactive[0][2] + inactive[0][3] - current_time == 0: break
        sepo = inactive.popleft()
        active.append(sepo)

    # 1. used 폐기 관리
    used = deque(sorted(used, key=lambda x: (x[2] + x[3] + x[3])))
    while used:
        if used[0][2] + used[0][3] * 2 == current_time:
            used.popleft()
        else:
            break

for tc in range(T):
    init()
    for current_time in range(1, K + 1):
        spread(current_time)
    answer = len(active) + len(used) + len(inactive)
    print('#{} {}'.format(tc+1, answer))
