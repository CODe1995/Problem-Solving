N = int(input())
field = [0]*N
answer = 0

def isValid(col):
    for i in range(col):
        # 조건1. 행이 겹치는가
        # 조건2. 열 차이가 행의 차이와 같은가
        if field[col] == field[i] or abs(col-i)==abs(field[col]-field[i]):
            return False
    return True

def action(col):
    global answer
    if col == N:
        answer += 1
        return
    for row in range(N):
        field[col] = row
        if isValid(col):
            action(col+1)

action(0)
print(answer)
