import sys,heapq
from collections import deque
input = sys.stdin.readline
xl = list()
yl = list()
zl = list()
N = int(input())
parent = [-1]*(N+1)
for i in range(N):
    a,b,c = map(int,input().strip().split())
    xl.append([a,i])
    yl.append([b,i])
    zl.append([c,i])
    parent[i]=i#init

def getParent(x):
    if(parent[x]==x):return x
    parent[x] = getParent(parent[x])
    return parent[x]

def unionParent(a,b):
    a = getParent(a)
    b = getParent(b)
    if a<b:parent[b]=a
    else:parent[a]=b

xl.sort()
yl.sort()
zl.sort()
dq = list()
for i in range(N-1):
    dq.append([xl[i+1][0]-xl[i][0],[xl[i][1],xl[i+1][1]]])#distance와 index a,b를 넣어준다.
    dq.append([yl[i+1][0]-yl[i][0],[yl[i][1],yl[i+1][1]]])
    dq.append([zl[i+1][0]-zl[i][0],[zl[i][1],zl[i+1][1]]])

answer = 0
dq.sort()
for i in range(len(dq)):
    d,[a,b] = dq[i]
    if getParent(a)==getParent(b):continue#이미연결
    unionParent(a,b)
    answer+=d
print(answer)
