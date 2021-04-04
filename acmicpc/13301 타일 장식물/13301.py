n = int(input())
dp = [0]*(81)
dp[1] = 4
dp[2] = 6
dp[3] = 10
for i in range(4,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])