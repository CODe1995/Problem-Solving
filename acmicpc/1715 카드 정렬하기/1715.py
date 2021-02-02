import heapq,sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
answer =0 
heapq.heapify(arr)#힙으로 변환
while(len(arr)>1):
    tmp=heapq.heappop(arr)+heapq.heappop(arr)
    answer+=tmp
    heapq.heappush(arr,tmp)
print(answer)