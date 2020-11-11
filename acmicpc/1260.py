from collections import deque
import sys
sys.setrecursionlimit(1000000)
#정점의 개수, 간선의 개수, 정점의 번호
N,M,V = map(int,sys.stdin.readline().split())
graph = {}
visited = [0] * (N+1)
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    if a not in graph: graph[a] = [b]
    elif b not in graph[a]: graph[a].append(b)
    if b not in graph: graph[b] = [a]
    elif a not in graph[b]: graph[b].append(a)
    #양방향 노드 추가

def dfs(root):
    if visited[root]==0:
        visited[root]=1
        print(root,end=' ')
        graph[root].sort()
        for i in graph[root]:
            if visited[i]==0:
                dfs(i)

def bfs(root):
    visited = [0]*(N+1)
    dq = deque([root])
    while dq:
        n = dq.popleft()
        visited[n] = 1
        print(n,end= ' ')
        graph[n].sort()
        for i in graph[n]:
            if visited[i]==0:
                dq.append(i)
                visited[i] = 1

    
dfs(V)
print()
bfs(V)