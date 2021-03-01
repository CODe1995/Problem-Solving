import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(float,input().strip().split())) for _ in range(N)]
dq = deque()
for i in range(N):#선 이어주기
    for j in range(i+1,N):
        dist = (abs(arr[i][0]-arr[j][0])**2+abs(arr[i][1]-arr[j][1])**2)**0.5
        dq.append([i,j,dist])#A to B : D(거리)
        dq = deque(sorted(dq,key = lambda x:x[2]))
parent = [i for i in range(N)]
def getParent(x):
    if parent[x]==x:return x
    parent[x] = getParent(parent[x])
    return parent[x]

def unionParent(a,b):
    a = getParent(a)
    b = getParent(b)
    if a<b: parent[b]=a
    else: parent[a]=b

qs = len(dq)
answer = 0
for i in range(qs):
    cur = dq.popleft()
    if getParent(cur[0])==getParent(cur[1]):continue#이미 연결된 경우
    unionParent(cur[0],cur[1])
    answer += cur[2]
# print(parent)
print("%.2f"%answer)