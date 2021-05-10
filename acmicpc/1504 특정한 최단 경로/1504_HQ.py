import heapq, sys
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

def dijkstra(start):
    d[start] = 0
    hq = []
    heapq.heappush(hq,[0,start])
    while hq:
        THIS = heapq.heappop(hq)
        cur = THIS[1]
        distance = THIS[0]

        if d[cur] < distance:continue
        if cur in edges:
            for _next,nextDistance in edges[cur]:
                if nextDistance + distance < d[_next]:
                    d[_next] = nextDistance + distance
                    heapq.heappush(hq,[d[_next],_next])

d = [10e9]*(N+1)
dijkstra(1) # 1 to goal1
case1 = d

d = [10e9]*(N+1)
dijkstra(mosts[0])  # goal1 to goal2
case2 = d

d = [10e9]*(N+1)
dijkstra(mosts[1])  # goal2 to N
case3 = d

answer = min(case1[mosts[0]]+case2[mosts[1]]+case3[N],case1[mosts[1]]+case3[mosts[0]]+case2[N])
print(answer if answer<10e9 else -1)