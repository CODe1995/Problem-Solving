import sys, heapq
input = sys.stdin.readline
N,K = map(int,input().split())
gems = [list(map(int,input().strip().split())) for _ in range(N)]    #보석[무게,가격]
bags = [int(input()) for _ in range(K)] #가방[무게]

gems = sorted(gems,key = lambda x:x[0])
bags.sort()
answer = 0

pq = []
cnt = 0
#작은 가방부터 채우기
for b in bags:
    while cnt<N and b>=gems[cnt][0]:
        heapq.heappush(pq,-gems[cnt][1])
        # print('added',gems[cnt][1])
        cnt+=1
    if pq:
        answer+=heapq.heappop(pq)
        # print('popoed',pq)
print(-answer)