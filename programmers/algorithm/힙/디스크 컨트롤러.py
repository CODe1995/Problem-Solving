# https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99

import heapq

def solution(jobs):
    answer = 0
    pq = []
    now = 0
    past = -1
    jobIndex = 0
    while jobIndex < len(jobs):
      # 현재 시점에서 수행 가능하고, 요청 종료가 더 빠른 케이스가 우선
      for job in jobs:
          if past < job[0] <= now:
            heapq.heappush(pq, (job[1], job[0]))
      if pq:
         job = heapq.heappop(pq)
         end = now + job[0]
         answer += end - job[1]
         past = now
         now += job[0]
         jobIndex += 1
      else:
         now += 1
    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))