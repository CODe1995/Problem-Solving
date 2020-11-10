import sys
sys.setrecursionlimit(10000)#재귀 제한
N,M = map(int,input().split())

def DFS(n):
    visited[n]=True
    for v in graph[n]:
        if not visited[v]:
            DFS(v)    
visited= []
visited = [False]*(N+1)
graph = {}

for _ in range(M):
    n1,n2 = map(int,input().split())
    if n1 not in graph:
        graph[n1]=[n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
    if n2 not in graph:
        graph[n2]=[n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

cnt = 0
for i in graph:
    if not visited[i]:#visited[i]가 False일 때(방문 안했을 때)
        DFS(i)
        cnt+=1
print(cnt)
    