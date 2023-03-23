def solution(queue1, queue2):    
    queue = queue1 + queue2
    avgSum = sum(queue) // 2 # 도달해야 하는 합
    
    start = 0
    end = len(queue1) - 1
    
    currentSum = sum(queue[start:end+1])
    
    answer = 0
    while start <= end and end < len(queue)-1:
        if currentSum == avgSum:
            return answer
        if currentSum < avgSum:
            end+=1
            currentSum += queue[end]
        elif currentSum > avgSum:
            currentSum -= queue[start]
            start+=1
        answer+=1
    return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]	))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]	))
print(solution([1, 1], [1, 10]	))
print(solution([1, 1,1,1], [1, 1,1,7]	))