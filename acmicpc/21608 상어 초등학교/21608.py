N = -1
students = {}
field = []
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def getBestSits(student_number: int) -> list:
    global students, N, direction, field
    favolist = students[student_number]
    max_score = 0
    max_empty_cnt = 0
    empty_xy = [-1, -1]
    # favo_sits
    # x좌표, y좌표, 주변공백수
    favo_sits = []
    for i in range(N):
        for j in range(N):
            if field[i][j] != 0: continue
            cur_score = 0
            empty_cnt = 0
            for dx, dy in direction:
                nx, ny = j + dx, i + dy
                if not (0 <= nx < N and 0 <= ny < N): continue
                if field[ny][nx] == 0:
                    empty_cnt += 1
                    continue
                if field[ny][nx] in favolist:
                    cur_score += 1
            if max_empty_cnt < empty_cnt:
                max_empty_cnt = empty_cnt
                empty_xy = [j, i]
            if empty_cnt == 0 and max_empty_cnt == 0 and empty_xy == [-1, -1]:
                empty_xy = [j, i]
            if cur_score == max_score:
                favo_sits.append([j, i, empty_cnt])
            elif cur_score > max_score:
                max_score = cur_score
                favo_sits.clear()
                favo_sits.append([j, i, empty_cnt])
    if not favo_sits or max_score == 0:
        favo_sits.clear()
        favo_sits.append(empty_xy)
    return favo_sits


def judgeSits(sits: list) -> list:
    if len(sits) == 1:
        return sits[0]
    else:
        sits.sort(key=lambda x: (-x[2], x[1], x[0]))
        # print('sits',sits)
        return sits[0]


def init():
    global students, N, field
    N = int(input())
    field = [[0] * N for _ in range(N)]
    for _ in range(N * N):
        inp = list(map(int, input().split()))
        students[inp[0]] = inp[1:]
        sit_list = getBestSits(inp[0])
        result = judgeSits(sit_list)
        # print(result)
        field[result[1]][result[0]] = inp[0]


def getScore():
    global field, students, N
    answer = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] == 0: continue
            cur = field[i][j]
            favolist = students[cur]
            favocnt = 0
            for dx, dy in direction:
                nx, ny = dx + j, dy + i
                if not (0 <= nx < N and 0 <= ny < N): continue
                if field[ny][nx] in favolist:
                    favocnt += 1
            answer += 10 ** (favocnt - 1) if favocnt > 0 else 0
    return answer


init()
print(getScore())
