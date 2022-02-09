import sys
from collections import deque
input = sys.stdin.readline
graph = []
parent = []
depthList = []
orderList = []
N = 0
M = 0


def init():
    global N, graph, M, parent, depthList
    N = int(input())
    graph = [list() for _ in range(N+1)]
    parent = [0]*(N+1)
    depthList = [0]*(N+1)
    for i in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    setDepth()
    M = int(input())
    for i in range(M):
        a,b = map(int,input().split())
        answer = lca(a,b)
        print(answer)

def lca(a, b):
    while depthList[a]!=depthList[b]:
        if depthList[a] < depthList[b]:
            b = parent[b]
        else:
            a = parent[a]
    while a!=b and a!=1 and b!=1:
        a = parent[a]
        b = parent[b]
    return a

def setDepth():
    global depthList
    dq = deque()
    dq.append(1)
    visited = [0]*(N+1)
    visited[1] = 1
    currentDepth = 1    
    while dq:
        qSize = len(dq)
        for i in range(qSize):
            num = dq.popleft()
            depthList[num] = currentDepth
            for _next in graph[num]:
                if visited[_next]:
                    continue
                visited[_next] = 1
                dq.append(_next)
                parent[_next] = num
        currentDepth+=1

if __name__ == "__main__":
    init()
