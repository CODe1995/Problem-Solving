N = int(input())
dp = [[0] * (N+1) for _ in range(101)]
arrHealth = list(map(int, input().split()))
arrHappy = list(map(int, input().split()))
for i in range(1, 100):
    for j in range(N):
      health = arrHealth[j]
      happy = arrHappy[j]
      if i >= health:
        dp[i][j] = max(dp[i-health][j-1] + happy, dp[i][j-1])
      else:
        dp[i][j] = dp[i][j-1]

print(dp[99][N-1])
