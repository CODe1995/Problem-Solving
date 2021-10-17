####
import sys

sys.stdin = open('C:/Users/code/source/repos/acmicpc/swea/5648 원자 소멸 시뮬레이션/sample_input.txt')
####

T = int(input())
N = -1
direction = [[0, -0.5], [0, 0.5], [-0.5, 0], [0.5, 0]]  # 상 하 좌 우
atoms = []


def init():
    global N, atoms
    N = int(input())
    atoms = []
    for _ in range(N):
        inp = list(map(int, input().split()))
        inp[0] += 1000
        inp[1] = abs(inp[1] - 1000)
        atoms.append(inp)  # x, y, d, k -> x, y, 방향, 에너지 크기


def solution():
    global atoms, N
    answer = 0
    for _ in range(4001):  # 최대 이동 횟수
        if len(atoms) <= 1: break
        field = dict()
        bomb = []
        for i in range(len(atoms)):
            nx = atoms[i][0] + direction[atoms[i][2]][0]
            ny = atoms[i][1] + direction[atoms[i][2]][1]
            atoms[i][0] = nx
            atoms[i][1] = ny
            if not (0 <= nx < 2001 and 0 <= ny < 2001):
                continue  # 필드밖
            number = atoms[i][0] + atoms[i][1] * 4001
            if number not in field:
                field[number] = [i]
            else:
                field[number].append(i)
                bomb.append(number)
        while bomb:
            bomb_number = bomb.pop()
            while field[bomb_number]:
                cur = field[bomb_number].pop()
                # atoms[cur][0], atoms[cur][1] = -1, -1  #폭발 처리
                answer += atoms[cur][3]
                atoms.pop(cur)
    return answer



for tc in range(1, T + 1):
    answer = -1
    init()
    answer = solution()
    print('#{} {}'.format(tc, answer))
