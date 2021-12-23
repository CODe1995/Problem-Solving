from collections import deque
N, M, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
fieldtemp = [[0]*M for _ in range(N)]  # 온도를 나타냄
W = int(input())
walls = [[[0, 0] for _ in range(M)] for _ in range(N)]
direction = [[], [1, 0], [-1, 0], [0, -1], [0, 1]]  # -,우좌상하
for _ in range(W):
    y, x, s = map(int, input().split())
    walls[y-1][x-1][s] = 1
willCheckTempPos = []
airconPos = []
for i in range(N):
    for j in range(M):
        if field[i][j] == 5:  # 온도 체크해야하는곳
            willCheckTempPos.append([j, i])
        elif field[i][j] in [1, 2, 3, 4]:  # 에어컨 위치
            airconPos.append([j, i])


def isCanGo(x1, y1, x2, y2):  # A지점에서 B지점까지 벽이 있는지 검사
    #방향은 총 4개
    #우측인 경우
    result = False
    if y1 == y2 and x1 < x2:
        result = False if walls[y1][x1][1] else True
    #좌측인 경우
    elif y1 == y2 and x1 > x2:
        result = False if walls[y2][x2][1] else True
    #아래쪽인 경우
    elif x1 == x2 and y1 < y2:
        result = False if walls[y2][x2][0] else True
    #위쪽인 경우
    elif x1 == x2 and y1 > y2:
        result = False if walls[y1][x1][0] else True
    return result

def isOutField(x,y):
    if not (0<=x<M and 0<=y<N):
        return True
    return False

def initAircon():   #에어컨 패턴 기억
    newTempField = [[0]*M for _ in range(N)]
    for air_x, air_y in airconPos:
        visited = [[0]*M for _ in range(N)] #자식들 안겹치게
        airconDir = field[air_y][air_x]
        dx, dy = direction[airconDir][0], direction[airconDir][1]
        start_x, start_y = dx +air_x, dy + air_y
        newTempField[start_y][start_x] += 5
        dq = deque()
        dq.append([start_x, start_y, 5])
        while dq:
            cx, cy, temp = dq.popleft()
            if temp == 1:
                continue

            #자식2 (중간)
            nx2, ny2 = cx+ dx, cy+dy
            if not isOutField(nx2,ny2) and isCanGo(cx,cy,nx2,ny2) and visited[ny2][nx2]==0: 
                newTempField[ny2][nx2]+=temp-1
                visited[ny2][nx2] = 1
                dq.append([nx2,ny2,temp-1])
            
            nextq = deque()
            if airconDir in [1,2]:   #우좌                
                nextq.append([cx, cy-1, cx+dx, cy-1])
                nextq.append([cx, cy+1, cx+dx, cy+1])
            elif airconDir in [3,4]:   #상하        
                nextq.append([cx-1, cy, cx-1, cy+dy])
                nextq.append([cx+1, cy, cx+1, cy+dy])

            while nextq:
                nx1,ny1,nx2,ny2 = nextq.popleft()
                if not isOutField(nx1,ny1) and isCanGo(cx,cy,nx1,ny1) and not isOutField(nx2,ny2) and isCanGo(nx1,ny1,nx2,ny2) and not visited[ny2][nx2]:
                    newTempField[ny2][nx2]+=temp-1
                    visited[ny2][nx2] = 1
                    dq.append([nx2,ny2,temp-1])
    return newTempField

def workAircon(temp):  # 에어컨 작동    
    #온도 적용
    for i in range(N):
        for j in range(M):
            fieldtemp[i][j] += temp[i][j]


def manageTemp():  # 온도 관리
    newTempField = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for dx, dy in direction[1:]:
                nx, ny = dx+j, dy+i
                if not (0 <= nx < M and 0 <= ny < N):
                    continue
                if not isCanGo(j, i, nx, ny):
                    continue
                curTemp = fieldtemp[i][j]
                nextTemp = fieldtemp[ny][nx]
                if curTemp <= nextTemp:
                    continue  # 온도차 없다면
                diff = (curTemp-nextTemp)//4
                newTempField[i][j] -= diff
                newTempField[ny][nx] += diff

    # 온도 적용
    for i in range(N):
        for j in range(M):
            if newTempField[i][j]+fieldtemp[i][j] < 0:
                fieldtemp[i][j] = 0
                continue
            fieldtemp[i][j] += newTempField[i][j]


def sideTempDown():
    for i in range(N):
        for j in range(M):
            if fieldtemp[i][j] == 0:
                continue
            if i == 0 and 0 <= j < M:
                fieldtemp[i][j] -= 1
            elif i == N-1 and 0 <= j < M:
                fieldtemp[i][j] -= 1
            elif j == 0 and 0 <= i < N:
                fieldtemp[i][j] -= 1
            elif j == M-1 and 0 <= i < N:
                fieldtemp[i][j] -= 1


def isTempGoal():
    for x, y in willCheckTempPos:
        if not fieldtemp[y][x] >= K:
            return False
    return True


def doSomthing():
    answer = 0
    rememberTemp = initAircon()
    while True:
        #1 바람나옴
        workAircon(rememberTemp)

        #2 온도 조절 Done.
        manageTemp()

        #3 1이상 외곽 1감소? Done.
        sideTempDown()

        #4 초콜릿?? Done.
        answer += 1
        if answer>100:
            break
        #5 모든칸 K 이상인지 검사 반복 Done.
        if isTempGoal():
            break
    print(answer)

doSomthing()