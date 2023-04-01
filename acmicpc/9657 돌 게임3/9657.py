N = int(input())
dp = [0] * (1001)

dp[2] = 1

for i in range(6, N+1):
    if dp[i-1] == 0 and dp[i-3] == 0 and dp[i-4] == 0:
      dp[i] = 1
print('SK' if dp[N] == 0 else 'CY')
