#21.02.02
import sys
import heapq
input = sys.stdin.readline

N = int(input())
rooms,query = [],[]
for _ in range(N):
    query.append(list(map(int,input().strip().split())))
query=sorted(query,key=lambda x:x[0])
for i in range(N):
    # print("i :",i,"rooms :",rooms,"Query :",query)
    if len(rooms)!=0 and rooms[0]<=query[i][0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms,query[i][1])
print(len(rooms))