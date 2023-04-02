import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        newScoville = a+b*2
        heapq.heappush(scoville, newScoville)
        answer += 1
    return answer
print(solution([1, 2, 3, 9, 10, 12], 7))