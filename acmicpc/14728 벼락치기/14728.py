N, T = map(int, input().split())
lists = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (T+1)

for cost, weight in lists:
    for j in range(T, cost-1, -1):
        dp[j] = max(dp[j - cost] + weight, dp[j])

print(dp[T])