import sys,math,copy
from collections import deque
input = sys.stdin.readline
direction = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
N,M,K = map(int,input().split())
field = [[deque() for _ in range(N)] for _ in range(N)]#질량, 속력, 방향

def solution():
    global field
    field_future = [[deque() for _ in range(N)] for _ in range(N)]
    divq = deque()       
    for i in range(N):
        for j in range(N):
            if field[i][j]:
                for cur_f in field[i][j]:
                    m,s,d = cur_f
                    #파이어볼 이동
                    nx,ny = (j+direction[d][0]*s)%(N),(i+direction[d][1]*s)%(N)#좌표보정
                    field_future[ny][nx].append([m,s,d])
                    if len(field_future[ny][nx])==2:#겹치는게 있다면?
                        divq.append([nx,ny])
                else:#모든 파이어볼을 미래 필드로 이동했다면 비워둔다.
                    field[i][j] = deque()
    while divq:#겹치는 파이어볼 처리
        dvx,dvy = divq.popleft()
        m,s,d = 0,0,-1
        odd,even = False,False
        for c in field_future[dvy][dvx]:#각각의 파이어볼에 접근
            m+=c[0]
            s+=c[1]
            if c[2]%2==0:even=True
            else:odd=True
        m = m//5#새로운 질량
        s = s//len(field_future[dvy][dvx])#새로운 속도
        field_future[dvy][dvx]=deque()#초기화
        if m == 0:continue
        if (odd and not even) or (even and not odd):d=0#새로운 방향 0,2,4,6
        else: d=1#1,3,5,7
        for new_d in [d,d+2,d+4,d+6]:
            field_future[dvy][dvx].append([m,s,new_d])
    field = copy.deepcopy(field_future)
        

if __name__ == "__main__":    
    for _ in range(M):
        y,x,m,s,d = map(int,input().strip().split())
        y-=1;x-=1
        field[y][x].append([m,s,d])
    for i in range(1,K+1):
        solution()
    answer = 0
    for i in range(N):
        for j in range(N):
            if field[i][j]:#field[i][j]가 존재한다면
                for c in field[i][j]:
                    answer+=c[0]#질량더해줌
    print(answer)