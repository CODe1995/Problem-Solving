N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
arr.sort()
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1,M+1):
        day, page = arr[j-1]
        if i >= day:
            dp[i][j] = max(dp[i][j-1], dp[i-day][j-1] + page)
        else:
            dp[i][j] = dp[i][j-1]
print(dp[N][M])