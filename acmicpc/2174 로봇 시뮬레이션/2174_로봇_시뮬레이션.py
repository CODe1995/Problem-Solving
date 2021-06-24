import sys
input = sys.stdin.readline
WIDTH, HEIGHT = map(int,input().split())
N,M = map(int,input().split())
field = [[0]*WIDTH for _ in range(HEIGHT)]
robots = []
orders = []
direction = {
    'E':[1,0],
    'W':[-1,0],
    'N':[0,1],  #N<->S 좌표 변경 (좌표계가 반대)
    'S':[0,-1]
}
turn = ['W','N','E','S']
    
robots.append([-1])#index 보정
for i in range(N):#로봇의 초기 위치
    x,y,d = input().strip().split()
    x = int(x)-1
    y = int(y)-1
    robots.append([x,y,d])
    field[y][x] = i+1
for i in range(M):#로봇의 명령
    idx,o,r = input().strip().split()
    orders.append([int(idx),o,int(r)])

def solution():
    for i in range(len(orders)):
        robot_id, order, rounds = orders[i]
        #L 왼쪽 90도 R 오른쪽 90도 F 직진
        if order == 'F':
            x,y,d = robots[robot_id]
            nx = x
            ny = y
            for rnd in range(rounds):
                nx += direction[d][0]
                ny += direction[d][1]
                if 0<=nx<WIDTH and 0<=ny<HEIGHT:
                    if field[ny][nx] == 0:#로봇의 성공적인 이동
                        field[y][x] = 0
                        field[ny][nx] = robot_id
                        x,y = nx,ny
                        robots[robot_id][0] = x
                        robots[robot_id][1] = y
                    else:#로봇과의 충돌
                        print('Robot {} crashes into robot {}'.format(robot_id,field[ny][nx]))
                        return False
                else:#벽과 충돌
                    print('Robot {} crashes into the wall'.format(robot_id))
                    return False
        elif order == 'L':
            for rnd in range(rounds):
                ci = turn.index(robots[robot_id][2])
                robots[robot_id][2] = turn[ci-1]
        elif order == 'R':
            for rnd in range(rounds):
                ci = turn.index(robots[robot_id][2])
                robots[robot_id][2] = turn[(ci+1)%4]
    return True

if solution():
    print('OK')