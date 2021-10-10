T = int(input())

for t in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1
    for c in coins:
        for i in range(c, M + 1):
            dp[i] += dp[i - c]
    print(dp[M])
