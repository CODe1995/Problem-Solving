import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]
dice = [
      [1],
    [4,5,3],
      [6],
      [2]
]

def right():
    dice[0][0],dice[1][0],dice[1][2],dice[2][0] = dice[1][0],dice[2][0],dice[0][0],dice[1][2]

def left():
    dice[0][0],dice[1][0],dice[1][2],dice[2][0] = dice[1][2],dice[0][0],dice[2][0],dice[1][0]

def up():
    dice[0][0],dice[1][1],dice[2][0],dice[3][0] = dice[1][1],dice[2][0],dice[3][0],dice[0][0]

def down():
    dice[0][0],dice[1][1],dice[2][0],dice[3][0] = dice[3][0],dice[0][0],dice[1][1],dice[2][0]

direction = [[0,-1],[1,0],[0,1],[-1,0]] # 북, 동, 남, 서

cur_d = 1 # 첫 시작은 동쪽으로
x,y = 0,0

def comp():
    global cur_d, field, dice, x, y
    bottom = dice[2][0]
    field_num = field[y][x]
    if bottom > field_num:
        cur_d = (cur_d+1) %4
    elif bottom < field_num:
        cur_d = cur_d - 1 if cur_d-1>=0 else 3

def bfs():
    global x,y,field
    dq = deque([[x,y]])
    cnt = 1
    visited = [[0]*M for _ in range(N)]
    visited[y][x] = 1
    while dq:
        cx,cy = dq.popleft()
        for dx,dy in direction:
            nx,ny = cx+dx, cy+dy
            if not (0<=nx<M and 0<=ny<N):
                continue
            if visited[ny][nx]: continue
            visited[ny][nx] = 1
            if field[y][x] == field[ny][nx]:
                dq.append([nx,ny])
                cnt+=1
    return cnt * field[y][x]

def moveCheck():
    global x,y,cur_d
    nx,ny = direction[cur_d][0]+x, direction[cur_d][1]+y
    if not (0<=nx<M and 0<=ny<N):   #필드밖
        if cur_d in [0,2]:
            cur_d = 2 if cur_d == 0 else 0
        else:
            cur_d = 1 if cur_d == 3 else 3

def gameStart():
    global cur_d,x,y
    answer = 0
    for i in range(K):
        moveCheck()
        if cur_d == 0:  #북
            up()
        elif cur_d == 1:
            right()
        elif cur_d == 2:
            down()
        else:
            left()
        x += direction[cur_d][0]
        y += direction[cur_d][1]
        comp()
        get_score = bfs()
        answer+=get_score
    print(answer)

gameStart()
        