import sys
from queue import PriorityQueue
input = sys.stdin.readline
N,E = map(int,input().split())
edges = dict()
for i in range(E):
    a,b,c = list(map(int,input().split()))
    if a in edges:edges[a].append([b,c])
    else:edges[a] = [[b,c]]
    if b in edges:edges[b].append([a,c])
    else:edges[b] = [[a,c]]
mosts = list(map(int,input().split()))
d = [10e9]*(N+1)

def dijkstra(start):
    d[start] = 0
    pq = PriorityQueue()
    pq.put([0,start])

    while pq.queue:
        THIS = pq.get()
        cur = THIS[1]
        distance = THIS[0]

        if d[cur] < distance:continue
        for i in range(len(edges[cur])):
            _next = edges[cur][i][0]#다음 노드 번호
            nextDistance = distance + edges[cur][i][1]

            if nextDistance < d[_next]:
                d[_next] = nextDistance
                pq.put([nextDistance,_next])

dijkstra(1) # 1 to goal1
case1 = d

d = [10e9]*(N+1)
dijkstra(mosts[0])  # goal1 to goal2
case2 = d

d = [10e9]*(N+1)
dijkstra(mosts[1])  # goal2 to N
case3 = d

answer = min(case1[mosts[0]]+case2[mosts[1]]+case3[N],case1[mosts[1]]+case3[mosts[0]]+case2[N])
print(answer)