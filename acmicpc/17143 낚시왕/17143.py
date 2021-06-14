import sys
input = sys.stdin.readline

R,C,M = map(int,input().split())#높이, 가로, 상어 수
field = [[0]*(C) for _ in range(R)]
direction = [[],[0,-1],[0,1],[1,0],[-1,0]]#1,2,3,4 상하우좌
for i in range(M):
    r,c,s,d,z = map(int,input().split())#위치, 속력, 방향, 크기
    r-=1#좌표 동기화(0index)
    c-=1
    #속력을 최소화 시킨다
    if d in [1,2]:#위아래
        s %= (R-1)*2
    else:#좌우
        s %= (C-1)*2
    field[r][c]=[r,c,s,d,z]

def changeDir(d):
    if d==1:return 2
    if d==2:return 1
    if d==3:return 4
    if d==4:return 3
def deepCopy(newfield):
    global field
    for i in range(R):
        for j in range(C):
            field[i][j]=newfield[i][j]
def moveSharks():#상어를 움직인다 동시에 포식한다
    global field,R,C
    newfield = [[0]*C for _ in range(R)]#상어 이동후
    for i in range(R):
        for j in range(C):
            if field[i][j]:#상어가 존재한다면?
                r,c,s,d,z = field[i][j]
                remain_s = s
                while remain_s:#상어의 위치이동
                    c+=direction[d][0]
                    r+=direction[d][1]
                    if C==c or R==r or -1==c or -1==r:#필드 벗어낫다?
                        d = changeDir(d)#방향 전환
                        if C==c:c-=2#좌표 반사
                        elif R==r:r-=2
                        elif c==-1:c+=2
                        elif r==-1:r+=2                            
                    remain_s-=1
                if newfield[r][c]:#이미 존재한다면?
                    if newfield[r][c][4]>z:#기존 상어가 크다면
                        continue
                newfield[r][c] = [r,c,s,d,z]
    deepCopy(newfield)#기존 field에 deepCopy해준다

hero = -1
answer = 0
def catchShark():
    global hero, field, answer
    for i in range(R):
        if field[i][hero]:#상어가 존재?
            size = field[i][hero][4]    #상어 크기 저장
            answer+=size
            field[i][hero]=[]
            return

def solution():
    global hero,R,C,answer
    while True:
        hero+=1 #1. 주인공의 우측 이동
        if hero==C:break
        catchShark()    #2. 주인공의 상어잡이
        moveSharks()    #3. 상어들의 이동
        # print(answer)    
    print(answer)
solution()