import sys
import heapq
input = sys.stdin.readline
N = int(input())
arr = [list(map(float,input().strip().split())) for _ in range(N)]
heap = []
for i in range(N):#선 이어주기
    for j in range(i+1,N):
        dist = (abs(arr[i][0]-arr[j][0])**2+abs(arr[i][1]-arr[j][1])**2)**0.5
        heapq.heappush(heap,[dist,i,j])#첫번째 요소에 비교값
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

qs = len(heap)
answer = 0
for i in range(qs):
    cur = heapq.heappop(heap)
    if getParent(cur[1])==getParent(cur[2]):continue#이미 연결된 경우
    unionParent(cur[1],cur[2])
    answer += cur[0]
# print(parent)
print("%.2f"%answer)