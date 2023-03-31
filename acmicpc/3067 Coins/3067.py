# https://velog.io/@uoayop/BOJ-3067-CoinsPython

for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    goal = int(input())
    # dp[i] = i원 동전을 이용해 j원을 만들 수 있는 경우의 수
    dp = [0] * (goal+1)
    dp[0] = 1
    for i in range(N):
        for j in range(coins[i], goal+1):
            dp[j] += dp[j - coins[i]]
    print(dp[goal])