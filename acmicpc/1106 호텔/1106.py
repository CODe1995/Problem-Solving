C, N = map(int,input().split())
lists = [list(map(int,input().split())) for _ in range(N)]
dp = [100000 for _ in range(C+100)]
dp[0] = 0

for cost, w in lists:
    for i in range(w, C+100):
        dp[i] = min(dp[i-w] + cost, dp[i])

print(min(dp[C:]))