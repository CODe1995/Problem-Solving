N = int(input())

dp = [10**6+1] * (N+1)
dp[1] = 0
for i in range(2, N+1):
    if i%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i%2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    dp[i] = min(dp[i-1]+1, dp[i])
print(dp[N])