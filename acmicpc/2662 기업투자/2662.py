from collections import deque
N, M = map(int, input().split())
arr = []
arr.append([0] * (M+1))
for i in range(N):
    arr.append([0] + list(map(int, input().split()))[1:])
dp = [[0] * (M+1) for _ in range(N+1)]
path = [[0] * (M+1) for _ in range(N+1)]
x,y = 0, 0
for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(1, i+1):
            val = dp[i-k][j-1] + arr[k][j]
            if val > dp[i][j]:
                dp[i][j] = val
                path[i][j] = k
            val = dp[i][j-1]
            if val > dp[i][j]:
                dp[i][j] = val
                path[i][j] = 0
                
print(dp[N][M])

q = []
remain = N
j = M
while len(q) < M:
    k = path[remain][j]
    q.append(str(k))
    remain -= k
    j -= 1
answer = ''
q.reverse()
    
print(' '.join(q))