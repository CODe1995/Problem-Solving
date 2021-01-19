##########################################################
import sys
from collections import deque
direction = [[0,1],[-1,0],[1,0],[0,-1]] #for BFS
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(ip())
def ips():return ip().split()
def ii():return int(input())
def mii():return map(int,ips())
def lmii():return list(mii())
##########################################################
height,width,D = mii()
field=[ lmii() for _ in range(height)]

#적군의 위치(x,y)를 반환한다.
#매개변수 : height의 위치, 궁수의 위치, 필드
def shoot(h_line,pos,s_field):
    for d in range(1,D+1):
        #왼쪽 우선 순위에 x:0도 있으므로 x가 큰 순부터 접근한다.
        for left in range(d,-1,-1):
            #거리의 차를 저장하고 탐색한다.
            diff = d-left
            #diff>0 : 0이 되어 버리면 현재 궁수의 위치와 겹치므로 0보다 커야한다.
            #0<=hdiff<height : 세로의 범위 체크
            #0<=wdiff<width : 가로의 범위 체크
            #s_board[hdiff][wdiff]==1 : 해당 좌표에 적군이 있다면
            hdiff = h_line - diff   #현재 위치(아처) ~ 해당 위치까지의 height(세로)
            wdiff = pos - left      #현재 위치(아처) ~ 해당 위치까지의 width(가로)
            if diff>0 and 0<=hdiff<height and 0<=wdiff<width and s_field[hdiff][wdiff]==1:
                return (wdiff,hdiff)#해당 x,y 좌표를 반환한다.            
        # 오른쪽은 왼쪽 이후에 실행하며
        # x:1부터 d까지 실행된다.
        for right in range(1,d+1):
            diff = d-right
            hdiff = h_line-diff
            wdiff = pos + right#우측이므로 left와 달리 더해야한다.
            if diff>0 and 0<=hdiff<height and 0<=wdiff<width and s_field[hdiff][wdiff]==1:
                return (wdiff,hdiff)            
    return None

#각 궁수 좌표에 대해 하나씩 처리하며,
#죽인 적의 수를 반환한다.
def simulation(pos):
    #deep copy를 쓰지 않아도 이런식으로 copy가 가능하다.
    c_field = [line[:] for line in field]
    killed_cnt = 0#죽인 적의 수(최종 반환 값)
    for n in range(height,-1,-1):#가장 아래쪽 필드부터 시작.
        killed_list = []#죽은 적군의 위치를 저장한다.(여러명)
        for p in pos:#세 명의 아처 위치(가로:x좌표)
            killed_enemy = shoot(n,p,c_field)#적 하나의 위치를 가져온다.(단일)
            if killed_enemy is not None:#죽인 적이 있다면
                killed_list.append(killed_enemy)
        
        for killed_enemy in killed_list:
            if c_field[killed_enemy[1]][killed_enemy[0]]==1:
                #해당 좌표의 적은 죽었으므로 0으로 바꿔줌
                c_field[killed_enemy[1]][killed_enemy[0]]=0
                killed_cnt+=1
    return killed_cnt

max_kill = 0
for i in range(width):
    for j in range(i+1,width):        
        for k in range(j+1,width):
            #항상 최댓값으로 유지한다.
            max_kill = max(max_kill,simulation([i,j,k]))
print(max_kill)