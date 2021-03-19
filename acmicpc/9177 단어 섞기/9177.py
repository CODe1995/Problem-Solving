import sys
from collections import deque

T = int(input())
for t in range(1,T+1):
    strA,strB,strC = input().strip().split()
    totalSize = len(strC)
    visited = [[0]*(len(strB)+1) for _ in range(len(strA)+1)]
    dq = deque([[0,0,0]])#Aidx, Bidx, Cidx
    visited[0][0]=1
    while dq:
        Aidx,Bidx,Cidx = dq.popleft()
        if len(strC)==Cidx:
            break
        if Aidx < len(strA) and strA[Aidx]==strC[Cidx] and visited[Aidx+1][Bidx]==0:
            dq.append([Aidx+1,Bidx,Cidx+1])
            visited[Aidx+1][Bidx]=1
        if Bidx < len(strB) and strB[Bidx]==strC[Cidx] and visited[Aidx][Bidx+1]==0:
            dq.append([Aidx,Bidx+1,Cidx+1])
            visited[Aidx][Bidx+1]=1
    print('Data set %d: %s'%(t,'yes' if visited[len(strA)][len(strB)] else 'no'))