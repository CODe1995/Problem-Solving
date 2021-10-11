N = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3


def solution(n):
    if dp[n]: return dp[n]
    dp[n] = (solution(n - 2) * 2 + solution(n - 1)) % 10007
    return dp[n]


solution(N)
print(dp[N])
