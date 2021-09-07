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
    #북
    newtemp = deepcopy(temp)
    dq = deque()    
    if d==0:
        for x in range(N):     
            for y in range(N):
                if newtemp[y][x]==0:
                    continue
                else:
                    dq.append(newtemp[y][x])
                    newtemp[y][x]=0
            for i in range(1,len(dq)):
                if dq[i-1]==dq[i] and dq[i]!=0:
                    dq[i-1]*=2   # 앞으로 합치고
                    dq[i]=0      # 뒤를 비움
            idx = 0
            while dq:
                nxt = dq.popleft()
                if nxt != 0:
                    newtemp[idx][x] = nxt
                    idx+=1
    elif d==2:
        for x in range(N):
            for y in range(N-1,-1,-1):
                if newtemp[y][x]==0:
                    continue
                else:
                    dq.append(newtemp[y][x])
                    newtemp[y][x]=0
            for i in range(1,len(dq)):
                if dq[i-1]==dq[i] and dq[i]!=0:
                    dq[i-1]*=2   # 앞으로 합치고
                    dq[i]=0      # 뒤를 비움
            idx = N-1
            while dq:
                nxt = dq.popleft()
                if nxt != 0:
                    newtemp[idx][x] = nxt
                    idx-=1
    elif d==1:#동
        for y in range(N):
            for x in range(N-1,-1,-1):
                if newtemp[y][x]==0:
                    continue
                else:
                    dq.append(newtemp[y][x])
                    newtemp[y][x]=0
            for i in range(1,len(dq)):
                if dq[i-1]==dq[i] and dq[i]!=0:
                    dq[i-1]*=2   # 앞으로 합치고
                    dq[i]=0      # 뒤를 비움
            idx = N-1
            while dq:
                nxt = dq.popleft()
                if nxt != 0:
                    newtemp[y][idx] = nxt
                    idx-=1
    elif d==3:#서
        for y in range(N):
            for x in range(N):
                if newtemp[y][x]==0:
                    continue
                else:
                    dq.append(newtemp[y][x])
                    newtemp[y][x]=0
            for i in range(1,len(dq)):
                if dq[i-1]==dq[i] and dq[i]!=0:
                    dq[i-1]*=2   # 앞으로 합치고
                    dq[i]=0      # 뒤를 비움
            idx = 0
            while dq:
                nxt = dq.popleft()
                if nxt != 0:
                    newtemp[y][idx] = nxt
                    idx+=1
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