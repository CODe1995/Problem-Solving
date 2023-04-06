# https://hongcoding.tistory.com/92
import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
  K = int(input().strip())
  maxPQ = []
  minPQ = []
  visited = [0] * (K+1)
  for i in range(K):
      sp = input().strip().split()
      command, number = sp[0], int(sp[1])
      if command == 'I':
          heapq.heappush(maxPQ, (-number, i))
          heapq.heappush(minPQ, (number, i))
          visited[i] = 1
      elif command == 'D':
          if number == 1:  # 최댓값 삭제
            while maxPQ and not visited[maxPQ[0][1]]:
                visited[maxPQ[0][1]] = 0
                heapq.heappop(maxPQ)
            if maxPQ:
                visited[maxPQ[0][1]] = 0
                heapq.heappop(maxPQ)
          else: # 최솟값 삭제
              while minPQ and not visited[minPQ[0][1]]:
                visited[minPQ[0][1]] = 0
                heapq.heappop(minPQ)
              if minPQ:
                visited[minPQ[0][1]] = 0
                heapq.heappop(minPQ)                 
  while maxPQ and not visited[maxPQ[0][1]]:
     heapq.heappop(maxPQ)
  while minPQ and not visited[minPQ[0][1]]:
     heapq.heappop(minPQ)
  if not maxPQ or not minPQ:
    print('EMPTY')
  else:
    print(-maxPQ[0][0], minPQ[0][0])
