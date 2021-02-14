import sys,copy
from collections import deque
direction = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

#방향을 45도 반시계 방향으로 바꿔주는 함수
def changeDir(d):
    return (d+1)%8

#물고기 이동시키는 함수
def moveFish(field,fishTable):
    for i in range(1,17):
        fx,fy = fishTable[i]#해당 위치의 물고기 좌표
        if fx==-1 and fy==-1:continue   #이미 상어에게 잡아먹힌 상태
        d = field[fy][fx][1]#해당 물고기의 방향
        origin_d = d#원래 방향
        nx,ny = fx+direction[d][0],fy+direction[d][1]
        while nx>=4 or ny>=4 or nx<0 or ny<0 or field[ny][nx][0]==0:
            #필드를 벗어나거나, 상어가 있는 경우
            d = changeDir(d)#방향을 튼다.
            if origin_d == d:#한바퀴 돈 경우(움직일 곳이 없음)
                break
            nx,ny = fx+direction[d][0],fy+direction[d][1]#바꾼 방향을 적용시킨다.
        else:
            field_status = field[ny][nx][0] #이동할 필드의 상태(물고기번호, 상어, -1{비었음})
            #하지만, 상어는 위 while문에서 걸러주기 때문에 여기선 넘어간다.
            if field_status==-1:#비어있는 필드라면
                fishTable[i]=[nx,ny]#좌표 갱신
                field[fy][fx]=[-1,-1]#기존에 있던 자리는 빈 필드로 설정                
                field[ny][nx]=[i,d]
            else:#다른 물고기라면
                fishTable[i],fishTable[field[ny][nx][0]]=fishTable[field[ny][nx][0]],fishTable[i]#fishTable 스왑
                field[fy][fx][1]=d#바뀐 방향을 갱신해준다.
                field[ny][nx],field[fy][fx]=field[fy][fx],field[ny][nx]#스왑
    return field, fishTable#바뀐 필드와 물고기 테이블을 반환한다.

#상어가 먹을 물고기가 있는지 확인하고 좌표를 반환하는 함수
def findFish(x,y,d,field):#상어의 좌표와 방향, 필드를 매개변수로 넣어준다.
    fishPos = []
    nx, ny = x+direction[d][0], y+direction[d][1]
    while 0<=nx<4 and 0<=ny<4:#필드 내
        if field[ny][nx][0]!=-1:#물고기라면?
            fishPos.append([nx,ny,field[ny][nx][1],field[ny][nx][0]])#물고기 좌표, 방향, 물고기번호
        nx+=direction[d][0]; ny+=direction[d][1]
    else:#빌드 밖
        return fishPos

#상어좌표 x,y, 바라보는 방향, 최대합, 지도, 물고기 번호가 담긴 좌표 테이블
def solution(x,y,d,maxsum,field,ft):
    fieldCopy = copy.deepcopy(field)#원본 필드는 영향이 가지 않게 deep copy
    fishTable = copy.deepcopy(ft)#물고기 번호별 좌표가 담긴 테이블 deep copy

    fieldCopy, fishTable = moveFish(fieldCopy,fishTable)#물고기 선 이동
    fishPos = findFish(x,y,d,fieldCopy)#상어가 먹을 수 있는 물고기 탐색
    answer = [0]
    while fishPos:
        nx,ny,nd,fishNum = fishPos.pop()#다음 좌표와 방향
        fishTable[fishNum]=[-1,-1]#먹음
        fieldCopy[ny][nx]=[0,nd]
        fieldCopy[y][x]=[-1,-1]
        answer.append(solution(nx,ny,nd,maxsum+fishNum,fieldCopy,fishTable))        
        fieldCopy[ny][nx]=[fishNum,nd]#복구
        fieldCopy[y][x]=[0,d]
        fishTable[fishNum]=[nx,ny]
    return max(answer+[maxsum])#최대값 반환

if __name__=="__main__":        
    origin_field = [[[-1,-1] for _ in range(4)] for _ in range(4)]
    fish = [[-1,-1] for _ in range(17)]
    psum=-1
    for i in range(4):
        tmp = list(map(int,input().split()))
        for j in range(4):
            if i==0 and j==0:#상어자리라면
                psum = tmp[j*2]#가장 처음 먹은 물고기의 번호를 저장
                origin_field[i][j]=[0,tmp[j*2+1]-1]#번호는 0(상어), 방향은 유지
                fish[tmp[0]]=[-1,-1]#해당 물고기는 잡아먹힌 것으로 설정.
            else:
                origin_field[i][j] = [tmp[j*2],tmp[j*2+1]-1]
                fish[origin_field[i][j][0]]=[j,i]#물고기번호별 좌표 삽입
    print(solution(0,0,origin_field[0][0][1],psum,origin_field,fish))