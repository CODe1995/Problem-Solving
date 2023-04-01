N = int(input())
mod = 10007

dp = [[0] * 10] + [[1] * 10] + [[0] * 10 for _ in range(N)]
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
        dp[i][j] %= mod
    
print(sum(dp[N]) % mod)