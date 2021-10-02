import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())

field = [list(map(int,input().strip().split())) for _ in range(N)]  #필드
# horseField = [[[]]*N for _ in range(N)]   #말의 인덱스를 필드위에 나타냄
horseField=[]
for i in range(N):
    horseField.append(list())
    for j in range(N):
        horseField[i].append(list())
horse = []  #각 말의 좌표와 방향값 관리

direction = [[1,0],[-1,0],[0,-1],[0,1]]
for i in range(K):
    y,x,d = map(int,input().split())
    horse.append([x-1,y-1,d-1])
    horseField[y-1][x-1].append(i)

def opposite(d):
    if d==0:return 1
    if d==1:return 0
    if d==2:return 3
    if d==3:return 2

def getHorseArrayFromField(index):
    x,y,d = horse[index]
    q = []
    while horseField[y][x]:
        curIndex = horseField[y][x].pop()
        q.append(curIndex)
        if curIndex == index:
            break
    return q[::-1]

def changeCoord(x,y,arrays):
    for i in range(len(arrays)):
        idx = arrays[i]
        horse[idx][0] = x
        horse[idx][1] = y
    return arrays

def checkRangeOut(x,y):
    return nx<0 or ny<0 or nx>=N or ny>=N

turn = 0
while turn<1000:
    turn+=1
    for curIndex in range(K):   #말 순서대로 돌아간다
        cur = horse[curIndex]
        cx,cy,cd = cur
        #0흰, 1빨, 2파
        nx,ny = cx+direction[cd][0], cy+direction[cd][1]  #다음 이동 좌표
        rangeOut = checkRangeOut(nx,ny)   #장외 = blue
        reverse = False
        doubleBlue = False
        if rangeOut or field[ny][nx]==2:# 파란색 처리
            cd = opposite(cd)   #반대 방향
            horse[curIndex][2]=cd
            nx,ny = cx+direction[cd][0], cy+direction[cd][1]  #이동 좌표
            rangeOut = checkRangeOut(nx,ny)
            if rangeOut or field[ny][nx]==2:
                nx,ny = cx,cy
                doubleBlue = True
        if field[ny][nx]==1 and not doubleBlue: #빨강            
            reverse=True
        
        #자식 말의 좌표 변경
        childHorse = getHorseArrayFromField(curIndex)        
        changeCoord(nx,ny,childHorse)
        horseField[ny][nx].extend(childHorse[::-1] if reverse else childHorse)
        if len(horseField[ny][nx])>=4:
            print(turn)
            sys.exit()
print(-1)