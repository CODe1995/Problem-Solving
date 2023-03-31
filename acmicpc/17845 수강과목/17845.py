N, K = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(K)]
dp = [0] * (N+1)
for i in range(K):
    weight, cost = arr[i]
    for j in range(N, -1, -1):
      if j >= cost:
          dp[j] = max(dp[j], dp[j-cost] + weight)
print(dp[N])