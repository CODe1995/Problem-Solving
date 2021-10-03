arr = list(map(int, input().split()))

# 출발,도착 포함 33개 / 자식 index, 자신 점수
field = {}
horses = [0, 0, 0, 0]
scores = []


def init_field():
    global field, scores
    scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, 13, 16, 19, 25, 22, 24,
              28, 27, 26, 30, 35]
    field = {}
    for i in range(21):
        lst = []
        for j in range(5):
            if i + j + 1 >= 21:
                lst.append(21)
                break
            else:
                lst.append(i + j + 1)
        field[i] = lst
    root1 = [5, 22, 23, 24, 25, 31, 32, 20, 21]
    root2 = [10, 26, 27, 25, 31, 32, 20, 21]
    root3 = [15, 28, 29, 30, 25, 31, 32, 20, 21]
    for i in range(len(root1)): field[root1[i]] = root1[i + 1:i + 6]
    for i in range(len(root2)): field[root2[i]] = root2[i + 1:i + 6]
    for i in range(len(root3)): field[root3[i]] = root3[i + 1:i + 6]


def dfs(depth, score):
    global arr, horses
    if depth == 10:
        return score
    dice = arr[depth]
    max_score = score
    for i in range(4):
        # 이미 끝에 도달한 말
        if horses[i] == 21:
            continue
        next_index = 0
        if len(field[horses[i]]) < dice:  # 끝에 도달한다는말
            next_index = 21
        else:
            next_index = field[horses[i]][dice-1]
        if next_index in horses and next_index != 21:
            continue
        cur_index = horses[i]
        horses[i] = next_index
        max_score = max(max_score, dfs(depth + 1, score + scores[next_index]))
        horses[i] = cur_index
    return max_score


def game():
    answer = dfs(0, 0)
    print(answer)


init_field()
game()
