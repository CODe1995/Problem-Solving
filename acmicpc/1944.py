##########################################################
import sys
from collections import deque
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
def lip():return list(input().rstrip())
##########################################################
direction = [[0,1],[1,0],[-1,0],[0,-1]]
n,m = mii()
field = [[0]*n for _ in range(n)]
cmaxk = 0
def bfs(x,y):
    global cmaxk
    #x,y,찾은Key수,움직인수,키가 있던 장소    
    dq = deque()
    dq.append([x,y,0,0])
    while dq:
        print(dq)
        # x,y,k,move = dq.popleft()           
        x,y,k,move = dq.popleft()           
        # print(x,y,k,move)
        for dx,dy in direction:
            nx = dx+x
            ny = dy+y
            if 0<=nx<n and 0<=ny<n and field[ny][nx]!='1':
                if field[ny][nx]=='K':
                    field[ny][nx]='1'
                    dq.append([nx,ny,k+1,move+1])
                    if cmaxk < k+1:
                        cmaxk=k+1                    
                    if m==k+1:
                        return move        
                else:
                    if cmaxk==k:
                        dq.append([nx,ny,k,move+1])
root=[-1,-1]
for i in range(n):
    field[i] = lip()
    if root==[-1,-1]:
        for yy,s in enumerate(field[i]):
            if s=='S':
                root=[yy,i]
                break
print(bfs(root[0],root[1]))