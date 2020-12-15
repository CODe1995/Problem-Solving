from collections import deque
def bfs(graph,root):
    visited = []
    dq = deque([root])
    while dq:#덱이 존재하면
        n = dq.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n])-set(visited))
                dq += tmp
    return len(visited) #최종적으로 방문한 노드의 개수만 반환                

cpnum = int(input())
conn = int(input())
root_node = 1
graph = {}
for _ in range(conn):
    a,b = map(int,input().split())
    if a not in graph:   #a 키가 생성되어있는지 먼저 확인
        graph[a]=[b]    #리스트로 추가해야함
    elif b not in graph[a]: #이미 있으면 추가
        graph[a].append(b)
    
    if b not in graph:  #양방향 그래프이므로 추가
        graph[b]=[a]
    elif a not in graph[b]:
        graph[b].append(a)
print(bfs(graph,1)-1)