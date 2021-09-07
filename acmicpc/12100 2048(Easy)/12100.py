from copy import deepcopy
from collections import deque
N = int(input())
field = [list(map(int,input().split())) for _ in range(N)]
direction = [[0,-1],[1,0],[0,1],[-1,0]] # 북동남서
answer = 0

def GetMaxBlock(temp):
    mx = 0
    for i in range(N):
        for j in range(N):
            mx = max(mx,temp[i][j])
    return mx

# 돌을 방향대로 움직임 (0-4,북동남서)
def MoveBlock(temp,d):
    newtemp = deepcopy(temp)
    dq = deque()    
    for x in range(N):     
        condition = range(N) if d in [0,3] else range(N-1,-1,-1)
        tx,ty = 0,0
        for y in condition:  # 0 to N-1 or N-1 to 0
            if d in [1,3]:
                tx,ty=y,x
            else:
                tx,ty=x,y
            if newtemp[ty][tx]==0:
                continue
            else:
                dq.append(newtemp[ty][tx])
                newtemp[ty][tx]=0
        for i in range(1,len(dq)):
            if dq[i-1]==dq[i] and dq[i]!=0:
                dq[i-1]*=2   # 앞으로 합치고
                dq[i]=0      # 뒤를 비움
        idx = 0 if d in [0,3] else N-1
        while dq:
            nxt = dq.popleft()
            if nxt != 0:
                if d in [0,2]:
                    newtemp[idx][tx] = nxt
                else:
                    newtemp[ty][idx] = nxt
                if d in [0,3]:idx+=1
                else: idx-=1
    return newtemp

def dfs(depth,temp):
    global answer
    if depth==5:
        answer = max(answer,GetMaxBlock(temp))
        return
    for i,[dx,dy] in enumerate(direction):
        newtemp = MoveBlock(temp,i)
        dfs(depth+1,newtemp)

dfs(0,field)
print(answer)