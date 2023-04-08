import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())

def bfs(x, graph, k):
    answer = 0
    dq = deque()
    visited = [0] * (N+1)
    dq.append(x)

    while dq:
        cur = dq.popleft()
        visited[cur] = 1
        for key in graph[cur]:
            value = graph[cur][key]
            if value >= k and not visited[key]:
                visited[key] = 1
                dq.append(key)
                answer += 1
    return answer

graph = {}
for _ in range(N-1):
    p, q, r = map(int, input().split())
    if p not in graph:
        graph[p] = {}
    if q not in graph:
        graph[q] = {}
    graph[p][q] = r
    graph[q][p] = r

for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(v, graph, k))
