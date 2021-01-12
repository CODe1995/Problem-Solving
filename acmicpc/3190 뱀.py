##########################################################
import sys
from collections import deque
# direction = [[0,1],[-1,0],[1,0],[0,-1]] #for BFS
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(ip())
def ips():return ip().split()
def ii():return int(input())
def mii():return map(int,ips())
def lmii():return list(mii())
##########################################################
n = ii()#보드의 크기
k = ii()#사과의 개수
field = [[0]*n for _ in range(n)]
for _ in range(k):
    a,b = mii()
    field[a-1][b-1]=1   #1은 사과
l = ii()#뱀의 방향 변환 횟수
turn = deque()
for _ in range(l):
    a,b = ips()
    turn.append([int(a),b])
turn = deque(sorted(turn,key=lambda x:x[0]))#시간순 정렬
def drcControl(direc,turnd):#현재 방향과 바꾸는 방향
    s = [[1,0],[0,1],[-1,0],[0,-1]]
    for i,[a,b] in enumerate(s):
        if [a,b]==direc:
            if turnd=='L':
                return s[i-1]
            else:
                if s==3:s=-1
                return s[i+1]
def solve():
    global k
    direction = [1,0]#오른쪽이 기본 방향
    q = deque([[0,0]])
    field[0][0]=2
    tailq = deque([[0,0]])
    move = 0
    while q:
        x,y = q.popleft()#머리
        tx,ty = tailq.popleft()#꼬리
        if turn and turn[0][0]==move:#방향 전환 먼저
            direction = drcControl(direction,turn[0][1])
            turn.popleft()
        dx,dy = direction
        nx,ny = dx+x,dy+y

        if 0>nx or nx>=n or 0>ny or ny>=n or field[ny][nx]>1:#엔딩 조건
            return move+1
        
        if field[ny][nx]==1:#사과를 만난 경우
            field[ny][nx]=2#그 자리에 머리를 넣어줌
            tailq.append([tx,ty])#꼬리는 그대로
            k-=1#사과 갯수 하나 감소
        else:#그냥 길인 경우
            field[ny][nx]=2#그 자리에 머리를 넣어줌
            field[ty][tx]=0#꼬리 있던 자리를 없애줌
            for tdx,tdy in [[0,1],[1,0],[-1,0],[0,-1]]:#다음 몸통 자리를 찾음
                ndx,ndy = tx+tdx,ty+tdy
                if field[ndy][ndx]==2:#몸통을 찾았다면
                    tailq.append([ndx,ndy])#그 몸통이 꼬리가 된다.
                    break            
        q.append([nx,ny])
        move+=1#시간 증가    
print(solve())
        
        
        
