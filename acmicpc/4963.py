import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
fields = list()
#대각선으로 이동 가능
direction = [[-1,-1],[-1,0],[0,-1],[1,1],[1,0],[0,1],[-1,1],[1,-1]]

def DFS(x,y):
    field[y][x]=0
    for dx,dy in direction:        
        nx = dx+x
        ny = dy+y
        if 0<=ny<h and 0<=nx<w and field[ny][nx]==1:
            DFS(nx,ny)

while True:
    w,h = map(int,input().split())
    if [w,h] == [0,0]:
        break
    field = [[-1]*w]*h
    for i in range(h):
        field[i] = list(map(int,input().split()))
    cnt = 0
    for i in range(w):
        for j in range(h):
            if field[j][i]==1:
                DFS(i,j)
                cnt+=1
    print(cnt)