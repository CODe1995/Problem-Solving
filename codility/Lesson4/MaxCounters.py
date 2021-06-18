def solution(N,A):
    savemaximum = 0
    maximum = 0
    counter = [0]*N
    for i in range(len(A)):
        if A[i]<=N:
            if counter[A[i]-1]<savemaximum:
                counter[A[i]-1]=savemaximum
            counter[A[i]-1]+=1
            maximum = max(counter[A[i]-1],maximum)
        else:# N보다 큰 수가 들어오면 maximum으로 동기화
            savemaximum = maximum
    for i in range(N):
        if counter[i]<savemaximum:
            counter[i]=savemaximum
    return counter

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))