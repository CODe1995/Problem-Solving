###
import sys
sys.stdin = open('C:/Users/code/source/repos/acmicpc/swea/5644 무선충전/sample_input.txt')
###

T = int(input())
M, BC = -1, -1
A, B = [], []
direction = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
BCarr = []
ax, ay = -1, -1
bx, by = -1, -1
answer = -1


def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def init():
    global M, BC, A, B, BCarr, ax, ay, bx, by, answer
    M, BC = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    BCarr = [list(map(int, input().split())) for _ in range(BC)]
    ax, ay, bx, by = 1, 1, 10, 10
    answer = 0


def calc_energy():
    global ax, ay, bx, by, answer
    aPossible = []
    bPossible = []
    for i in range(len(BCarr)):
        bcx, bcy, dist, energy = BCarr[i]  # BC의 좌표와 거리, 충전량
        aDist = get_distance(bcx, bcy, ax, ay)
        bDist = get_distance(bcx, bcy, bx, by)
        if aDist <= dist:
            aPossible.append([i, energy])
        if bDist <= dist:
            bPossible.append([i, energy])
    if aPossible:
        aPossible.sort(key=lambda x: (-x[1], x[0]))
    if bPossible:
        bPossible.sort(key=lambda x: (-x[1], x[0]))

    maxEnergy = 0

    if aPossible and bPossible:
        for i in range(len(aPossible)):
            for j in range(len(bPossible)):
                if aPossible[i][0] == bPossible[j][0]:  # 두개 겹친다?
                    maxEnergy = max(maxEnergy, aPossible[i][1])
                else:
                    maxEnergy = max(maxEnergy, aPossible[i][1] + bPossible[j][1])
    elif aPossible:
        maxEnergy += aPossible[0][1]
    elif bPossible:
        maxEnergy += bPossible[0][1]
    answer += maxEnergy
    # print(maxEnergy)


def move(time: int):
    global ax, ay, bx, by, direction
    ax += direction[A[time]][0]
    ay += direction[A[time]][1]
    bx += direction[B[time]][0]
    by += direction[B[time]][1]


for tc in range(1, T+1):
    init()
    for time in range(M):
        calc_energy()
        move(time)
    calc_energy()
    print('#{} {}'.format(tc, answer))
