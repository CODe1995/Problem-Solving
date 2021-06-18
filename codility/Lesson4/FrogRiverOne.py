def solution(X,A):
    visited = [0]*100001
    sec = 0    
    for i in range(len(A)):
        sec+=1
        if not visited[A[i]]:
            visited[A[i]]=1
            X-=1
            if not X:
                return sec-1
    return -1
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))