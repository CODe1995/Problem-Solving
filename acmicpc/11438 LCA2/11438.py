from collections import deque
from math import log2
import sys
input = sys.stdin.readline
N = -1
M = -1
logN = -1
nodes = list()
parents = list()
depths = list()


def init():
    global N, M, nodes, parents, logN, depths
    N = int(input())
    logN = int(log2(N) + 1)
    nodes = [[] for _ in range(N+1)]
    depths = [0] * (N+1)
    depths[1] = 1

    parents = [[0 for i in range(logN)] for _ in range(N+1)]
    parents[1][0] = 1

    for i in range(N-1):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)

    setParentAndDepth()
    for i in range(1, logN):
        for j in range(1, N+1):
            parents[j][i] = parents[parents[j][i-1]][i-1]

    M = int(input())
    for i in range(M):
        a, b = map(int, input().split())
        print(getLca(a,b))


def getLca(a, b):
    if depths[a] > depths[b]:
        a,b= b,a 
    for i in range(logN-1,-1,-1):
        if depths[b] - depths[a] >= 1<<i:
            b = parents[b][i]
    if a==b:
        return a
    for i in range(logN-1,-1,-1):
        if parents[a][i] != parents[b][i]:
            a = parents[a][i]
            b = parents[b][i]
    return parents[a][0]


def setParentAndDepth():
    visited = [0]*(N+1)
    dq = deque()
    dq.append(1)
    visited[1] = 1
    while(dq):
        cur = dq.popleft()
        for child in nodes[cur]:
            if visited[child]:
                continue
            visited[child] = 1
            parents[child][0] = cur
            depths[child] = depths[cur]+1
            dq.append(child)


if __name__ == '__main__':
    init()
