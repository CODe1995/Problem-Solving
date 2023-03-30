from collections import deque

N, M = map(int, input().split())
graph = {}
for _ in range(M):
    u, v = map(int, input().split())
    if u in graph: graph[u].append(v)
    else: graph[u] = [v]
    if v in graph: graph[v].append(u)
    else: graph[v] = [u]

dq = deque()
visited = [0] * (N+1)
answer = 0

for num in range(1, N+1):
    if visited[num]:
        continue
    if num not in graph:
        answer += 1
        continue
    dq.append(num)
    visited[num] = 1
    while dq:
        currentNum = dq.popleft()
        for nextNum in graph[currentNum]:
            if not visited[nextNum]:
                visited[nextNum] = 1
                dq.append(nextNum)
    answer+=1
print(answer)
