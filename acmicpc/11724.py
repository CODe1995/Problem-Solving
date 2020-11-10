import sys
sys.setrecursionlimit(10000)#재귀 제한
N,M = map(int,sys.stdin.readline().split())

def DFS(n):
    visited[n]=True
    for v in graph[n]:
        if not visited[v]:
            DFS(v)    
visited= []
visited = [False]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    n1,n2 = map(int,sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

cnt = 0
for i in range(1,N+1):
    if not visited[i]:#visited[i]가 False일 때(방문 안했을 때)
        DFS(i)
        cnt+=1
sys.stdout.write(str(cnt))    