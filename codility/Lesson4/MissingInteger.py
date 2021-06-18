def solution(A):
    visited = [0]*1000001
    for i in A:
        if i>0:#음수는 생각하지 않는다
            visited[i]=1
    for i in range(1,len(visited)):
        if not visited[i]:
            return i

print(solution([1,2,3]))
print(solution([-1,-3]))
print(solution([1,3,6,4,1,2]))
print(solution([1000000,2,1]))