import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
graph = []
for i in range(N):
    for j in range(N):
        if i==j:continue
        graph.append([i,j,arr[i][j]])#i to j 행성, 가치
parent = [i for i in range(N)]
def find(x):
    if x==parent[x]:return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:return False
    if a<b:parent[b]=a
    else: parent[a]=b
    return True
graph = sorted(graph,key = lambda x:x[2])#거리순 정렬
answer = 0
for cur in graph:
    a,b,d = cur
    if union(a,b):
        answer+=d
print(answer)