arr = list(map(int, input().split()))

# 출발,도착 포함 33개 / 자식 index, 자신 점수
field = [[0, 0]] * 33
horses = [0, 0, 0, 0]


def init_field():
    global field
    for i in range(0, 21):
        field[i] = [[i + 1, i * 2]]
    field[5].append([22, 13])
    field[22], field[23], field[24] = [[23, 13]], [[24, 16]], [[25, 19]]
    field[10].append([26, 20])
    field[26], field[27] = [[27, 22]], [[25, 24]]
    field[15].append([28, 30])
    field[28], field[29], field[30] = [[29, 28]], [[30, 27]], [[25, 26]]
    field[25], field[31], field[32] = [[31, 25]], [[32, 30]], [[20, 35]]
    field[21] = [[-1, 0]]


def get_score(current_position):
    global field
    return field[current_position][0][1]


def move(current_position, move_count, first_move):
    if move_count == 0 or current_position == 21:
        return current_position
    if first_move and len(field[current_position]) == 2:  # 지름길 있는 경우
        return move(field[current_position][1][0], move_count - 1, False)
    return move(field[current_position][0][0], move_count - 1, False)


def check_overlay(index):
    global horses
    for i in range(4):
        if index == horses[i] and index != 21:
            return False
    return True


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
        next_index = move(horses[i], dice, True)
        if not check_overlay(next_index):
            continue
        cur_index = horses[i]
        horses[i] = next_index
        max_score = max(max_score, dfs(depth + 1, score + get_score(next_index)))
        horses[i] = cur_index
    return max_score


def game():
    answer = dfs(0, 0)
    print(answer)


init_field()
game()
