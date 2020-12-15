import sys
from collections import deque
sys.setrecursionlimit(100000)
direction = [[1,0],[0,1],[-1,0],[0,-1]]
def DFS(root):    #visited 반환
    _x,_y = root
    field[_y][_x] = 0
    for dx,dy in direction:
        nx = _x+dx
        ny = _y+dy
        if 0<= ny < len(field) and 0<=nx < len(field[0]):
            # 배추가 심어져있으면
            if field[ny][nx]==1:
                DFS([nx,ny])

T = int(sys.stdin.readline())
for _ in range(T):
    stack = []  #배추가 있는 곳 저장        
    M,N,K = map(int,sys.stdin.readline().split())  #가로,세로,배추갯수
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        n1,n2 = map(int,sys.stdin.readline().split())
        stack.append([n1,n2])   #배추가 있는 좌표값 저장
        field[n2][n1] = 1
    cnt = 0
    for [x,y] in stack:
        if field[y][x] == 1:    #배추가 심어져 있으면
            cnt+=1
            DFS([x,y])    #방문
    print(cnt)