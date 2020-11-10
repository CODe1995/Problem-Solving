from collections import deque

#정점의 개수, 간선의 개수, 정점의 번호
N,M,V = map(int,input().split())
lst = list()
for i in range(M):
    lst.append(list(map(int,input().split())))


def dfs(graph,root):
    visited = []
    stack = [root]
    while stack:
        n = stack.pop()
        
    return

def bfs(graph,root):
    return

print(dfs(lst,V))
print(bfs(lst,V))