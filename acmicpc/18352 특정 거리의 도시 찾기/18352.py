import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
N,M,K,X = map(int,input().split())
graph = dict()
for i in range(M):
    a,b = map(int,input().split())
    if a in graph:graph[a].append(b)
    else: graph[a] = [b]
answer = []
visited = [0]*300001
def bfs():
    dq = deque([[X,0]])    
    while dq:
        cur,depth = dq.popleft()
        if depth==K:
            answer.append(cur)
        if cur in graph:
            for _next in graph[cur]:
                if visited[_next]:continue
                if depth+1>K:continue
                visited[_next]=1
                dq.append([_next,depth+1])
        
bfs()
if len(answer)==0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)